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
    obj = HeroImage(text="",image="")
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