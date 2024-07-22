from django.contrib import admin
from .models import Order, Product, Category, Review, OrderItem, User, Payment


# Register your models here.
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(OrderItem)
admin.site.register(User)
admin.site.register(Payment)
