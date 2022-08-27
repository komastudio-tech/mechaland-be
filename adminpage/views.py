from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from mechaland.models import *
from mechaland.forms import *

# Create your views here.

# HOME
@login_required(login_url="/login/")
def index(request):
    return render(request, "index.html")

# HOME --- Hero Image
@login_required(login_url="/login/")
def heroimg(request):
    context={}
    context["dataset"] = HeroImage.objects.all().reverse()
    return render(request, "heroimg.html", context)

@login_required(login_url="/login/")
def heroimg_change(request, id):
    context={}
    heroimg = HeroImage.objects.get(id=id)
    obj = heroimg
    form = HeroImageForm(request.POST or None,request.FILES or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('/heroimg')
    context['form'] = form
    context['formtitle'] = 'Ubah Hero Image'
    return render(request, "forms-change.html", context)

@login_required(login_url="/login/")
def heroimg_add(request):
    context={}
    obj = HeroImage(text="",buy_text="",image="")
    form = HeroImageForm(request.POST or None,request.FILES or None,instance = obj)
    if form.is_valid():
        form.save()
        return redirect('/heroimg')
    context['form'] = form
    context['formtitle'] = 'Tambah Hero Image'
    return render(request, "forms.html", context)

@login_required(login_url="/login/")
def heroimg_delete(request, id):
    context ={}
    heroimg = HeroImage.objects.get(id=id)
    context["deleteTitle"] = 'Delete Hero Image'
    context["data"] = heroimg
    if request.method =="POST":
        heroimg.delete()
        return redirect('/heroimg')
    return render(request, "delete.html", context)

# HOME --- Featured Collection
@login_required(login_url="/login/")
def featured_collection(request):
    context={}
    context["dataset"] = FeaturedCollection.objects.all().reverse()
    return render(request, "featured-collection.html", context)

@login_required(login_url="/login/")
def featured_collection_change(request, id):
    context={}
    featured_collection = FeaturedCollection.objects.get(id=id)
    obj = featured_collection
    form = FeaturedCollectionForm(request.POST or None,request.FILES or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('/featured-collection')
    context['form'] = form
    context['formtitle'] = 'Ubah Featured Collection'
    return render(request, "forms-change.html", context)

@login_required(login_url="/login/")
def featured_collection_add(request):
    context={}
    obj = HeroImage(text="",buy_text="", image="")
    form = FeaturedCollectionForm(request.POST or None,request.FILES or None,instance = obj)
    if form.is_valid():
        form.save()
        return redirect('/featured-collection')
    context['form'] = form
    context['formtitle'] = 'Tambah Featured Collection'
    return render(request, "forms.html", context)

@login_required(login_url="/login/")
def featured_collection_delete(request, id):
    context ={}
    featured_collection = FeaturedCollection.objects.get(id=id)
    context["deleteTitle"] = 'Delete Featured Collection'
    context["data"] = featured_collection
    if request.method =="POST":
        heroimg.delete()
        return redirect('/featured-collection')
    return render(request, "delete.html", context)