from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')

def shop(request):
    return render(request, 'shop.html')

def checkout(request):
    return render(request, 'checkout.html')

def single_product(request):
    return render(request, 'single-product.html')

def cart(request):
    return render(request, 'cart.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')
def login_Signup(request):
    return render(request, 'loginSignup.html')
