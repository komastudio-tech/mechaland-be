from .models import *
from rest_framework import serializers

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id','url', 'name','image', 'ranking')

class ProductSerializer(serializers.ModelSerializer):
    list_photos = ProductImageSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ('id','url', 'title','description', 'specs', 'price','stock','category','list_photos')

class InterestCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterestCheck
        fields = ('id','url', 'title','image', 'text', 'created_at')

class HeroImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroImage
        fields = ('id','url', 'text','buy_text', 'image')

class FeaturedCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeaturedCollection
        fields = ('id','url', 'text','buy_text', 'image')