from django.urls import path
from .views import *

urlpatterns = [
    path('/', index, name="index"),
    path('about/', about, name='about'),
    path('farm-shop/', farm_shop, name="farm_shop"),
    path('contact/', contact, name='contact'),
    
    path('product/<str:slug>', single_product, name="single_product"),
    path('product/category/<str:category>', product_category, name="product_category"),

    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),

    path('wishlist/', wishlist, name='wishlist'),
    path('shopping-cart/', shopping_cart, name='shopping_cart'),
    path('add-to-cart/', add_to_cart, name="add_to_cart"),
    path('checkout/', checkout, name='checkout'),

    path('error/', error, name='error_page'),
]
