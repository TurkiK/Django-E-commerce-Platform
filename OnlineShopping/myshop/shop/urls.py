from django.urls import path
from . import views
from .views import add_balance, change_password, order_detail

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('home/', views.home, name='home'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('products/<str:category_name>/', views.products, name='products'),
    path('add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('add_to_cart_home/<int:pk>/', views.add_to_cart_home, name='add_to_cart_home'),
    path('remove_from_cart/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('rate_product/<int:pk>/', views.rate_product, name='rate_product'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('checkout/', views.checkout, name='checkout'),
    path('order_history/', views.order_history, name='order_history'),
    path('add_balance/', add_balance, name='add_balance'),
    path('user_info/', views.user_info, name='user_info'),
    path('change-password/', change_password, name='change_password'),
    path('order_detail/<int:order_id>/', order_detail, name='order_detail'),
]
