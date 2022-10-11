from django.db import models
import uuid
import datetime

# Create your models here.
# HOME
class HeroImage(models.Model):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    text = models.CharField(max_length=500)
    buy_text = models.CharField(max_length=500)
    image = models.FileField(upload_to='back-end-image/HeroImage/', blank = False)

    class Meta:
        managed = True
        db_table = 'hero-image'

    def __str__(self) -> str:
        return self.text

class FeaturedCollection(models.Model):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    text = models.CharField(max_length=500)
    buy_text = models.CharField(max_length=500)
    image = models.FileField(upload_to='back-end-image/FeaturedCollection/', blank = False)

    class Meta:
        managed = True
        db_table = 'featured-collection'

    def __str__(self) -> str:
        return self.text

#GROUP-BUY
class Product(models.Model):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=500, blank=True, verbose_name='Description')
    link = models.CharField(max_length=500, blank=False)
    has_specs = models.BooleanField(default=False, blank=False)
    has_variant = models.BooleanField(default=False, blank=False)
    price = models.IntegerField(blank=True)
    stock = models.IntegerField(blank=True)
    category = models.CharField(max_length=100, blank=False)

    class Meta:
        managed = True
        db_table = 'product'
        unique_together=('category', 'title')

    def __str__(self) -> str:
        return self.title

class ProductSpecs(models.Model):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    specs = models.CharField(max_length=500, blank=False, verbose_name='Specs')
    product = models.ForeignKey(Product, related_name='list_specs', on_delete=models.CASCADE)
    class Meta:
        managed = True
        db_table = 'product-specs'
        unique_together=('specs', 'product')

    def __str__(self) -> str:
        return self.specs

class ProductVariant(models.Model):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    name = models.CharField(max_length=500, blank=False)
    variant = models.CharField(max_length=500, blank=False)
    price = models.IntegerField()
    stock = models.IntegerField()
    product = models.ForeignKey(Product, related_name='list_variant', on_delete=models.CASCADE)
    class Meta:
        managed = True
        db_table = 'product-variant'
        unique_together=('variant', 'product')
    def __str__(self) -> str:
        return self.name
    
class ProductImage(models.Model):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    name = models.CharField(max_length=500, blank=False)
    image = models.FileField(upload_to='back-end-image/ProductImage/', blank = False)
    ranking = models.IntegerField()
    product = models.ForeignKey(Product, related_name='list_photos', on_delete=models.CASCADE)

    class Meta:
        ordering = ('ranking', )
        managed = True
        db_table = 'product-image'

    def __str__(self) -> str:
        return self.name

class InterestCheck(models.Model):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    title = models.CharField(max_length=200, blank=False)
    text = models.CharField(max_length=1000, blank=False)
    discord = models.CharField(max_length=1000, blank=True)
    image = models.FileField(upload_to='back-end-image/InterestCheck/', blank = False)

    class Meta:
        managed = True
        db_table = 'interest-check'

    def __str__(self) -> str:
        return self.title

class Updates(models.Model):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    title = models.CharField(max_length=200, blank=False)
    text = models.CharField(max_length=1000, blank=False)
    category = models.CharField(max_length=100, blank=False)

    class Meta:
        managed = True
        db_table = 'updates'

    def __str__(self) -> str:
        return self.title