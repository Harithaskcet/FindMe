from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from products.models import Products
# Create your views here.
def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password= request.POST['inputPassword'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request,'login.html',{'error':'Please Check your username and password'}) 
    else:
        return render(request, 'login.html')

def signUp(request):
    if request.method == 'POST':
        if request.POST['inputPassword'] == request.POST['pwd']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request,'signUp.html',{'error':'Username is already taken'}) 
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],request.POST['pwd'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request,'signUp.html',{'error':'Passwords must match'}) 
    else:
        return render(request,'signUp.html')

def logOut(request):
    if request.method == 'POST':
        products = Products.objects
        for product in products.all():
            product.upvoted = False
            product.save()
        auth.logout(request)
        return redirect('home')