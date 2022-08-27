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

    
]
