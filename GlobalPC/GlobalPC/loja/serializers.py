from rest_framework import serializers
from .models import Product, Category, SubCategory

# Serializers, One


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price']


class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategory
        fields = ['id', 'title']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'title']


# Serializers, More than One
class ProductSubCategoryBrandSerializer(serializers.ModelSerializer):
    subcategory = serializers.StringRelatedField(many=False)
    brand = serializers.StringRelatedField(many=False)

    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'subcategory', 'brand']


class SubCategoryProductSerializer(serializers.ModelSerializer):
    subcategory_products = serializers.StringRelatedField(many=True)

    class Meta:
        model = SubCategory
        fields = ['id', 'title', 'subcategory_products']


class CategorySubCategorySerializer(serializers.ModelSerializer):
    category_subcategory = serializers.StringRelatedField(many=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'category_subcategory']
