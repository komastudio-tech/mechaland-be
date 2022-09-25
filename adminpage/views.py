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
    obj = FeaturedCollection(text="",buy_text="", image="")
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
        featured_collection.delete()
        return redirect('/featured-collection')
    return render(request, "delete.html", context)

# UPDATES
@login_required(login_url="/login/")
def updates(request):
    context={}
    context["dataset"] = Updates.objects.all().reverse()
    return render(request, "updates.html", context)

@login_required(login_url="/login/")
def updates_change(request, id):
    context={}
    updates = Updates.objects.get(id=id)
    obj = updates
    form = UpdatesForm(request.POST or None,request.FILES or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('/updates')
    context['form'] = form
    context['formtitle'] = 'Ubah Updates'
    return render(request, "forms-change.html", context)

@login_required(login_url="/login/")
def updates_add(request):
    context={}
    obj = Updates(title="",text="", category="")
    form = UpdatesForm(request.POST or None,request.FILES or None,instance = obj)
    if form.is_valid():
        form.save()
        return redirect('/updates')
    context['form'] = form
    context['formtitle'] = 'Tambah Updates'
    return render(request, "forms.html", context)

@login_required(login_url="/login/")
def updates_delete(request, id):
    context ={}
    updates = Updates.objects.get(id=id)
    context["deleteTitle"] = 'Delete Updates'
    context["data"] = updates
    if request.method =="POST":
        updates.delete()
        return redirect('/updates')
    return render(request, "delete.html", context)

# INTEREST CHECK
@login_required(login_url="/login/")
def interest_check(request):
    context={}
    context["dataset"] = InterestCheck.objects.all().reverse()
    return render(request, "interest-check.html", context)

@login_required(login_url="/login/")
def interest_check_change(request, id):
    context={}
    interest_check = InterestCheck.objects.get(id=id)
    obj = interest_check
    form = InterestCheckForm(request.POST or None,request.FILES or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('/interest-check')
    context['form'] = form
    context['formtitle'] = 'Ubah Interest Check'
    return render(request, "forms-change.html", context)

@login_required(login_url="/login/")
def interest_check_add(request):
    context={}
    obj = InterestCheck(title="",text="", discord="", image="")
    form = InterestCheckForm(request.POST or None,request.FILES or None,instance = obj)
    if form.is_valid():
        form.save()
        return redirect('/interest-check')
    context['form'] = form
    context['formtitle'] = 'Tambah Interest Check'
    return render(request, "forms.html", context)

@login_required(login_url="/login/")
def interest_check_delete(request, id):
    context ={}
    interest_check = InterestCheck.objects.get(id=id)
    context["deleteTitle"] = 'Delete Interest Check'
    context["data"] = interest_check
    if request.method =="POST":
        interest_check.delete()
        return redirect('/interest-check')
    return render(request, "delete.html", context)

# PRODUCT
@login_required(login_url="/login/")
def product(request):
    context={}
    context["dataset"] = Product.objects.all().order_by('category')
    return render(request, "product.html", context)

@login_required(login_url="/login/")
def product_change(request, id):
    context={}
    product = Product.objects.get(id=id)
    obj = product
    form = ProductForm(request.POST or None,request.FILES or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('/product')
    context['form'] = form
    context['formtitle'] = 'Ubah Product'
    return render(request, "forms-change.html", context)

@login_required(login_url="/login/")
def product_add(request):
    context={}
    obj = Product(title="",description="", has_specs="", has_variant="", category="", price="", stock="")
    form = ProductForm(request.POST or None,request.FILES or None,instance = obj)
    if form.is_valid():
        form.save()
        return redirect('/product')
    context['form'] = form
    context['formtitle'] = 'Tambah Product'
    return render(request, "forms.html", context)

@login_required(login_url="/login/")
def product_delete(request, id):
    context ={}
    product = Product.objects.get(id=id)
    context["deleteTitle"] = 'Delete Product'
    context["data"] = product
    if request.method =="POST":
        product.delete()
        return redirect('/product')
    return render(request, "delete.html", context)

# PRODUCT IMAGE
@login_required(login_url="/login/")
def product_image(request,id):
    context={}
    product = Product.objects.get(id=id)
    context["dataset"] = ProductImage.objects.all().filter(product=product).order_by('ranking')
    context["product"] = product
    return render(request, "product-image.html", context)

@login_required(login_url="/login/")
def product_image_change(request, id):
    context={}
    product_image = ProductImage.objects.get(id=id)
    obj = product_image
    form = ProductImageForm(request.POST or None,request.FILES or None, instance = obj)
    if form.is_valid() and ProductImage.objects.filter(ranking=request.POST.get('ranking')).exists():
        product_image_prev_ranking = ProductImage.objects.get(id=id).ranking
        target_product_image = ProductImage.objects.get(ranking = request.POST.get('ranking'), product= request.POST.get('product'))
        target_product_image.ranking = 99999
        target_product_image.save(update_fields=['ranking'])
        form.save()
        target_product_image.ranking = product_image_prev_ranking
        target_product_image.save(update_fields=['ranking'])
    if form.is_valid():
        form.save()
        return redirect('/product-image/'+ str(obj.product.id))
    context['form'] = form
    context['formtitle'] = 'Ubah Product'
    return render(request, "forms-change.html", context)

@login_required(login_url="/login/")
def product_image_add(request,id):
    context={}
    product =Product.objects.get(id=id)
    obj = ProductImage(name="",image="", ranking="", product=product)
    form = ProductImageForm(request.POST or None,request.FILES or None,instance = obj)
    if form.is_valid() and ProductImage.objects.filter(ranking=request.POST.get('ranking'), product=Product.objects.get(id=id)).exists():
        target_product_image = ProductImage.objects.get(ranking = request.POST.get('ranking'), product= request.POST.get('product'))
        target_product_image.ranking = ProductImage.objects.filter(product=Product.objects.get(id=id)).latest('ranking').ranking + 1
        target_product_image.save(update_fields=['ranking'])
        form.save()
    if form.is_valid():
        form.save()
        return redirect('/product-image/'+str(product.id))
    context['form'] = form
    context['formtitle'] = 'Tambah Product Image'
    return render(request, "forms.html", context)

@login_required(login_url="/login/")
def product_image_delete(request, id):
    context ={}
    product_image = ProductImage.objects.get(id=id)
    context["deleteTitle"] = 'Delete Product Image'
    context["data"] = product_image
    if request.method =="POST":
        product_image.delete()
        return redirect('/product-image/'+str(product_image.product.id))
    return render(request, "delete.html", context)

# PRODUCT SPECS
@login_required(login_url="/login/")
def product_specs(request,id):
    context={}
    product = Product.objects.get(id=id)
    context["dataset"] = ProductSpecs.objects.all().filter(product=product)
    context["product"] = product
    return render(request, "product-specs.html", context)

@login_required(login_url="/login/")
def product_specs_change(request, id):
    context={}
    product_specs = ProductSpecs.objects.get(id=id)
    obj = product_specs
    form = ProductSpecsForm(request.POST or None,request.FILES or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('/product-specs/'+ str(obj.product.id))
    context['form'] = form
    context['formtitle'] = 'Ubah Product Specs'
    return render(request, "forms-change.html", context)

@login_required(login_url="/login/")
def product_specs_add(request,id):
    context={}
    product =Product.objects.get(id=id)
    obj = ProductSpecs(specs="", product=product)
    form = ProductSpecsForm(request.POST or None,request.FILES or None,instance = obj)
    if form.is_valid():
        form.save()
        return redirect('/product-specs/'+str(product.id))
    context['form'] = form
    context['formtitle'] = 'Tambah Product Specs'
    return render(request, "forms.html", context)

@login_required(login_url="/login/")
def product_specs_delete(request, id):
    context ={}
    product_specs = ProductSpecs.objects.get(id=id)
    context["deleteTitle"] = 'Delete Product Specs'
    context["data"] = product_specs
    if request.method =="POST":
        product_specs.delete()
        return redirect('/product-specs/'+str(product_specs.product.id))
    return render(request, "delete.html", context)

# PRODUCT VARIANT
@login_required(login_url="/login/")
def product_variant(request,id):
    context={}
    product = Product.objects.get(id=id)
    context["dataset"] = ProductVariant.objects.all().filter(product=product)
    context["product"] = product
    return render(request, "product-variant.html", context)

@login_required(login_url="/login/")
def product_variant_change(request, id):
    context={}
    product_variant = ProductVariant.objects.get(id=id)
    obj = product_variant
    form = ProductVariantForm(request.POST or None,request.FILES or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('/product-variant/'+ str(obj.product.id))
    context['form'] = form
    context['formtitle'] = 'Ubah Product Variant'
    return render(request, "forms-change.html", context)

@login_required(login_url="/login/")
def product_variant_add(request,id):
    context={}
    product =Product.objects.get(id=id)
    obj = ProductVariant(variant="",price="",stock="", product=product)
    form = ProductVariantForm(request.POST or None,request.FILES or None,instance = obj)
    if form.is_valid():
        form.save()
        return redirect('/product-variant/'+str(product.id))
    context['form'] = form
    context['formtitle'] = 'Tambah Product Variant'
    return render(request, "forms.html", context)

@login_required(login_url="/login/")
def product_variant_delete(request, id):
    context ={}
    product_variant = ProductVariant.objects.get(id=id)
    context["deleteTitle"] = 'Delete Product Variant'
    context["data"] = product_variant
    if request.method =="POST":
        product_variant.delete()
        return redirect('/product-variant/'+str(product_variant.product.id))
    return render(request, "delete.html", context)

