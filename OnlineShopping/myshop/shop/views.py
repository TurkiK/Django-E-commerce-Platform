from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Product, Order, OrderItem, UserProfile
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from decimal import Decimal


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user, balance=1000)  # Start with a default balance
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('home')


@login_required
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


@login_required
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})


@login_required
def add_to_cart(request, pk):
    if request.method == "POST":
        quantity = int(request.POST.get('quantity', 1))  # Get the quantity from the form, default to 1 if not found
        product = Product.objects.get(pk=pk)
        cart = request.session.get('cart', {})

        if str(pk) in cart:
            cart[str(pk)]['quantity'] += quantity
        else:
            cart[str(pk)] = {'price': float(product.price), 'quantity': quantity}

        request.session['cart'] = cart
        return redirect('cart_detail')
    return redirect('product_detail', pk=pk)


@login_required
def cart_detail(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())
    total_price = 0
    cart_items = []

    for product in products:
        item = {
            'product': product,
            'quantity': cart[str(product.id)]['quantity'],
            'subtotal': cart[str(product.id)]['quantity'] * product.price
        }
        total_price += item['subtotal']
        cart_items.append(item)

    return render(request, 'cart_detail.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

def remove_from_cart(request, pk):
    cart = request.session.get('cart', {})

    if str(pk) in cart:
        del cart[str(pk)]
        request.session['cart'] = cart

    return redirect('cart_detail')


@login_required
def checkout(request):
    user_profile = UserProfile.objects.get(user=request.user)
    cart = request.session.get('cart', {})
    total_price = Decimal('0.00')  # Initialize total_price as Decimal

    # Calculate total price
    for pk, details in cart.items():
        total_price += Decimal(details['quantity']) * Decimal(details['price'])

    if user_profile.balance >= total_price:
        order = Order.objects.create(user=request.user, total_price=total_price, is_completed=True)
        for pk, details in cart.items():
            product = Product.objects.get(pk=pk)
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=details['quantity']
            )
        user_profile.balance -= total_price  # Ensure total_price is a Decimal
        user_profile.save()
        request.session['cart'] = {}  # Clear the cart
        return redirect('order_history')
    else:
        return render(request, 'checkout.html', {'error': 'Insufficient funds'})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order_history.html', {'orders': orders})