from .models import *
from .serializers import *
from rest_framework import viewsets, views, status, generics
from django_filters.rest_framework import DjangoFilterBackend

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('category')
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']
    http_method_names = ['get']

class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all().order_by('ranking')
    serializer_class = ProductImageSerializer
    http_method_names = ['get']

class ProductSpecsViewSet(viewsets.ModelViewSet):
    queryset = ProductSpecs.objects.all()
    serializer_class = ProductSpecsSerializer
    http_method_names = ['get']

class ProductVariantViewSet(viewsets.ModelViewSet):
    queryset = ProductVariant.objects.all().order_by('variant')
    serializer_class = ProductVariantSerializer
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

class UpdatesViewSet(viewsets.ModelViewSet):
    queryset = Updates.objects.all()
    serializer_class = UpdatesSerializer
    http_method_names = ['get']