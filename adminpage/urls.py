# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from adminpage import views

app_name = "adminpage"

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # HOME --- Hero Image
    path('heroimg', views.heroimg, name='heroimg'),
    path('heroimg-add', views.heroimg_add, name='heroimg-add'),
    path('heroimg/delete/<id>', views.heroimg_delete, name='heroimg-delete'),
    path('heroimg/change/<id>', views.heroimg_change, name='heroimg-change'),

    # HOME --- Featured Collection
    path('featured-collection', views.featured_collection, name='featured-collection'),
    path('featured-collection-add', views.featured_collection_add, name='featured-collection-add'),
    path('featured-collection/delete/<id>', views.featured_collection_delete, name='featured-collection-delete'),
    path('featured-collection/change/<id>', views.featured_collection_change, name='featured-collection-change'),

    # UPDATES
    path('updates', views.updates, name='updates'),
    path('updates-add', views.updates_add, name='updates-add'),
    path('updates/delete/<id>', views.updates_delete, name='updates-delete'),
    path('updates/change/<id>', views.updates_change, name='updates-change'),

    # INTEREST CHECK
    path('interest-check', views.interest_check, name='interest-check'),
    path('interest-check-add', views.interest_check_add, name='interest-check-add'),
    path('interest-check/delete/<id>', views.interest_check_delete, name='interest-check-delete'),
    path('interest-check/change/<id>', views.interest_check_change, name='interest-check-change'),

    # PRODUCT
    path('product', views.product, name='product'),
    path('product-add', views.product_add, name='product-add'),
    path('product/delete/<id>', views.product_delete, name='product-delete'),
    path('product/change/<id>', views.product_change, name='product-change'),

    # PRODUCT IMAGE
    path('product-image/<id>', views.product_image, name='product-image'),
    path('product-image-add/<id>', views.product_image_add, name='product-image-add'),
    path('product-image/delete/<id>', views.product_image_delete, name='product-image-delete'),
    path('product-image/change/<id>', views.product_image_change, name='product-image-change'),

    # PRODUCT SPECS
    path('product-specs/<id>', views.product_specs, name='product-specs'),
    path('product-specs-add/<id>', views.product_specs_add, name='product-specs-add'),
    path('product-specs/delete/<id>', views.product_specs_delete, name='product-specs-delete'),
    path('product-specs/change/<id>', views.product_specs_change, name='product-specs-change'),

    # PRODUCT VARIANT
    path('product-variant/<id>', views.product_variant, name='product-variant'),
    path('product-variant-add/<id>', views.product_variant_add, name='product-variant-add'),
    path('product-variant/delete/<id>', views.product_variant_delete, name='product-variant-delete'),
    path('product-variant/change/<id>', views.product_variant_change, name='product-variant-change'),
]
