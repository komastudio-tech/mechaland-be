from .models import *
from .serializers import *
from rest_framework import viewsets, views, status, generics

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get']

class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all().order_by('ranking').reverse()
    serializer_class = ProductImageSerializer
    http_method_names = ['get']

class InterestCheckViewSet(viewsets.ModelViewSet):
    queryset = InterestCheck.objects.all()
    serializer_class = InterestCheckSerializer
    http_method_names = ['get']

class HeroImageViewSet(viewsets.ModelViewSet):
    queryset = HeroImage.objects.all()
    serializer_class = HeroImageSerializer
    http_method_names = ['get']

class FeaturedCollectionViewSet(viewsets.ModelViewSet):
    queryset = FeaturedCollection.objects.all()
    serializer_class = FeaturedCollectionSerializer
    http_method_names = ['get']