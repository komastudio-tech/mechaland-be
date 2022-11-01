from .models import *
from rest_framework import serializers

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id','url', 'name','image', 'ranking')

class ProductSpecsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSpecs
        fields = ('id','url', 'specs')

class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ('id','url', 'variant','price', 'stock')

class ProductSerializer(serializers.ModelSerializer):
    list_photos = ProductImageSerializer(many=True, read_only=True)
    list_specs = ProductSpecsSerializer(many=True, read_only=True)
    list_variant = ProductVariantSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ('id','url', 'title', 'price','stock','category','has_variant','has_specs', 'link', 'link_source', 'list_photos', 'list_specs', 'list_variant')

class InterestCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterestCheck
        fields = ('id','url', 'title','image', 'price', 'discord')

class HeroImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroImage
        fields = ('id','url', 'text','buy_text', 'image')

class FeaturedCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeaturedCollection
        fields = ('id','url', 'text','buy_text', 'image')

class UpdatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Updates
        fields = ('id','url', 'title','text', 'category')