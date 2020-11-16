from django.db import models
from django.db.models.base import Model

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, blank=False,unique=True)
    unit_cost = models.DecimalField(max_digits=9, decimal_places=2, blank=False)
    markup_price = models.DecimalField(max_digits=9, decimal_places=2, blank=False)
    weight = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to="products/images")
    unit_quantity = models.CharField(max_length=100)
    description = models.TextField(default='')
    is_active = models.BooleanField(default=True)
    sku = models.CharField(max_length=20, blank=True)
    slug = models.SlugField(blank=True)
    

    # foreign keys
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = self.name.replace(" ", "-")

        return super(Product, self).save(*args, **kwargs)


class ProductReview(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=True)
    review = models.TextField(blank=False)


class Category(models.Model):
    name = models.CharField(max_length=50, blank=False)
    date_created = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    date = models.DateField(auto_now=True)
    is_complete = models.BooleanField(default=False)
    is_pickup =  models.BooleanField(default=False)
    order_no = models.CharField(max_length=10)
    cusomter_name = models.CharField(max_length=200, blank=False)
    contact = models.CharField(max_length=15, blank=False)
    location = models.CharField(max_length=200, blank=False)
    email = models.EmailField()
    geolocation = models.CharField(max_length=50)

    def __str__(self):
        return self.order_no

    def save(self, *args, **kwargs):
        count = len(self.id)
        new_id = ''

        if count == 1:
            new_id = f'000{self.id}'
        elif count == 2:
            new_id = f'00{self.id}'
        elif count == 3:
            new_id = f'0{self.id}'
        else:
            new_id = self.id            

        self.order_no = f"pgl{new_id}"

        return super(Order, self).save(*args, **kwargs)


class OrderDetail(models.Model):
    quantity = models.IntegerField()
    unit_price = models.DecimalField(decimal_places=2, max_digits=9)

    # foreign keys
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)


class TempCart(models.Model):
    name = models.CharField(max_length=100)
    pId = models.IntegerField()
    qty = models.IntegerField(default=0)
    price = models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
        return self.temp_id