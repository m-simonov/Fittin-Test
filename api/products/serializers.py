from rest_framework import serializers

from products.models import Category, Offer, Product


class CategoryShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class ProductListSerializer(serializers.ModelSerializer):
    category = CategoryShortSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        exclude = ['product']


class ProductSerializer(serializers.ModelSerializer):
    offers = OfferSerializer(many=True)
    category = CategoryShortSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'
