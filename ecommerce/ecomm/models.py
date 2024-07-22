from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name}"

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Order(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user} {self.total_amount}"

class OrderItem(models.Model):
    quantity = models.PositiveIntegerField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    order = models.ForeignKey(Order, related_name='order_items', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name} {self.quantity}"

class Review(models.Model):
    comment = models.TextField()
    rating = models.PositiveIntegerField()
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} {self.product.name}"

class Payment(models.Model):
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} {self.balance}"
