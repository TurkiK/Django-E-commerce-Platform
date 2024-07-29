from rest_framework import serializers
from .models import Product, Category, Order, OrderItem, Review
from django.db.models import Avg

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'product', 'content', 'rating']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )
    reviews = ReviewSerializer(many=True, read_only=True, source='review_set')
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'category', 'category_id', 'reviews', 'average_rating']

    def get_average_rating(self, obj):
        average_rating = obj.review_set.aggregate(Avg('rating'))['rating__avg'] or 0
        return round(average_rating, 1)

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source='product', write_only=True
    )

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'product_id', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(source='orderitem_set', many=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'total_price', 'items']
