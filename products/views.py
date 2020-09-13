from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Products
# Create your views here.

def home(request):
    products = Products.objects
    return render(request, 'productPage.html', { 'products': products })

def detail(request, product_id):
    product_detail = get_object_or_404(Products, pk=product_id)
    return render(request, 'detail.html', {'product': product_detail})

@login_required(login_url="/account/login")
def addVote(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Products, pk=product_id)
        product.votes_total += 1
        product.upvoted = True
        product.save()
        return redirect('/product/' + str(product.id))

@login_required(login_url="/account/login")
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            product = Products()
            product.title = request.POST['title']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url = request.POST['url']
            else:
                product.url = 'http://' + request.POST['url']
            product.pub_date = timezone.datetime.now()
            product.votes_total = 1
            product.body = request.POST['body']
            product.iconImage = request.FILES['icon']
            product.image = request.FILES['image']
            product.changedBy = request.user
            product.upvoted = False
            product.save()
            return redirect('/product/' + str(product.id))
        else:
            return render(request, 'create.html', { 'error: All the fields are required' })
    else:
        return render(request, 'create.html')
