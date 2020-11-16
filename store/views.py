from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
# from django.db.models import Sum, F
# from django.forms.models import model_to_dict

from .models import *

# Create your views here.
def farm_shop(request):
    return render(request, 'farmshop.html')


@require_GET
def index(request):
    query = Product.objects.filter(is_active=True).all()
    categories = Category.objects.all()
    return render(request, 'index.html', {'products': query, 'categories': categories})


@require_POST
@csrf_exempt
def add_to_cart(request):
    # add item to 'cart'
    temp, created = TempCart.objects.get_or_create(
        pId=request.POST['pId'],
        name=request.POST['name'],
        price=request.POST['price'],
    )

    if created:
        # when a new item is created, return the entire item
        temp.qty = 1
        temp.save()
        print('created')
        return JsonResponse({"status": 'created'}, status=200)

    # if the selected item already exists, just add one to
    # its quantity n return the new qty
    temp.qty += 1
    temp.save()
    print('already exist')
    return JsonResponse({"status": "exist"}, status=200)



@require_GET
def single_product(request, slug):
    try:
        prod = Product.objects.get(slug=slug)
        return render(request, 'single-product.html', {'product':prod})
    except Product.DoesNotExist:
        return redirect("/error")


def shopping_cart(request):
    cart = TempCart.objects.all()
    return render(request, 'shopping-cart.html', {'cart': cart})


def product_category(request, category):
    items = Product.objects.filter(category__name=category).all()
    return render(request, 'categories.html', {'items':items, 'category':category})


def about(request):
    return render(request, 'about.html')

def error(request):
    return render(request, 'error.html')


def contact(request):
    return render(request, 'contact.html')


@csrf_exempt
def checkout(request):
    if request.method=="GET":
        return render(request, 'checkout.html')
    
    TempCart.objects.all().delete()
    return render(request, 'order-confirmed.html')


    # return JsonResponse({"status": 'Done'}, status=200)

def signup(request):
    return render(request, 'signup.html')

def signin(request):
    return render(request, 'signin.html')

def wishlist(request):
    return render(request, 'wishlist.html')