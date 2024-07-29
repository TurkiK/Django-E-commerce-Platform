from django.contrib import admin
from .models import Product, ProductImage, Category, Order, OrderItem, UserProfile, Review

# Admin for Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category, CategoryAdmin)

# Admin for Product
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # Number of extra forms to display

class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
    ]
    list_display = ('name', 'price', 'stock', 'category')

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)

# Inline admin for Order Items within the Order admin
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

# Admin for Order
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'total_price', 'is_completed']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)

# Admin for OrderItem
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity']
    list_filter = ['order', 'product']

admin.site.register(OrderItem, OrderItemAdmin)

# Admin for UserProfile
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'balance']
    search_fields = ['user__username', 'user__email']

admin.site.register(UserProfile, UserProfileAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'rating', 'created_at']
    list_filter = ['product', 'user']

admin.site.register(Review, ReviewAdmin)
