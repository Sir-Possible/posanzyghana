from django import forms
from .models import Product, Order, OrderDetail


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name','unit_cost','markup_price','weight','unit_quantity','description', 'category')

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('date','order_no','customer_name','contact','location','email','geolocation')

class OrderDetailForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields = ('quantity','unit_price','item','order')
