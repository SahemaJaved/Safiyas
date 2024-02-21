from urllib import request

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404

from .models import Category, Product, CartItem
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


# Create your views here.
# venv- newsafenv
#view for product display
def allproducts(request, slug_c=None):
    page_c=None
    products=None
    if slug_c!=None:
        page_c=get_object_or_404(Category, slug=slug_c)
        products=Product.objects.all().filter(category=page_c,available=True)
    else:
        products=Product.objects.all().filter(available=True)

    return render(request,'home.html',{'category':page_c,'products':products})


def prod_det(request, slug_c, slug_p ):

    try:
        product=Product.objects.get(category__slug=slug_c, slug=slug_p )
    except Exception as e:
        raise e
    return render(request, 'product.html', {'product':product})



#view for authentication
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname= request.POST['fname']
        lname=request.POST['lname']
        email= request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name= fname
        myuser.last_name=lname

        myuser.save()

        return redirect('signin')

    return render(request, 'registration.html')


def signin(request):

    if request.method == "POST":
        username= request.POST['username']
        password1=request.POST['password1']

        user = authenticate(username=username, password=password1)

        if user is not None:
            login(request, user)
            fname=user.first_name
            return redirect('allproducts')


        else:
            messages.error(request, "Invalid Credentials")
            return redirect('allproducts')

    return render(request, 'signin.html')
def signout(request):
    logout(request)
    return redirect('allproducts')



#view for cart

def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product,
                                                        user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('view_cart')


def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('view_cart')

def home(request):
    return render(request,'home.html')
def about_us(request):
    return render(request,'about-us.html')
def feed_back(request):
    return render(request,'feedback.html')

