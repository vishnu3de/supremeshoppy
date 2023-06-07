import datetime

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

#adress-------------------------------------------------------------

class ResAddress(models.Model):
    housename = models.CharField(max_length=200)
    area = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    pincode = models.IntegerField()
    username = models.ForeignKey(User, on_delete=models.CASCADE)


class ShiAddress(models.Model):
    housename = models.CharField(max_length=200)
    area = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    pincode = models.IntegerField()
    username = models.ForeignKey(User, on_delete=models.CASCADE)

class Complaint(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.subject

#--------------------------------------------------------------------

#product-------------------------------------------------------------

class ProductsName(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class offername(models.Model):
    name = models.CharField(max_length=100)
    productsname = models.ForeignKey(ProductsName, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class suboffer(models.Model):
    name = models.CharField(max_length=100)
    productsname = models.ForeignKey(ProductsName, on_delete=models.CASCADE)
    offername = models.ForeignKey(offername, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class category(models.Model):
    productsname = models.ForeignKey(ProductsName, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Product(models.Model):
    productsname = models.ForeignKey(ProductsName, on_delete=models.CASCADE)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    offername = models.ForeignKey(offername, on_delete=models.CASCADE)
    suboffer = models.ForeignKey(suboffer, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="static/images")
    image1 = models.ImageField(upload_to="static/images")
    image2 = models.ImageField(upload_to="static/images")
    name = models.CharField(max_length=100)
    availability = models.BooleanField(default=True)
    price = models.IntegerField(default=0)
    brand = models.CharField(max_length=100)
    dprice = models.IntegerField()
    description = models.CharField(max_length=400)

    def __str__(self):
        return self.name

class Size(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

#order-------------------------------------------------------------


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    orderid=models.CharField(max_length=50 , null=True,blank=True)
    status_pay=models.CharField(max_length=50, null=True,blank=True)
    paid=models.BooleanField(default=False)


class Order(models.Model):
    image=models.ImageField(upload_to="static/images/orders")
    product= models.CharField(max_length=200)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    payment=models.ForeignKey(Payment, on_delete=models.CASCADE,blank=True)
    orderid=models.CharField(max_length=50 , null=True,blank=True)
    quantity=models.CharField(max_length=5)
    price=models.IntegerField()
    total=models.IntegerField()
    address=models.CharField(max_length=300)
    date=models.DateField(default=datetime.datetime.today)
    size = models.CharField(max_length=12,blank=True)
    status=models.BooleanField(default=False)
    picked = models.BooleanField(default=False)
    otw = models.BooleanField(default=False)
    pickup = models.BooleanField(default=False)

    def __str__(self):
        return self.product




class orderdetailadmin(models.Model):
    ids=models.CharField(max_length=5)
    deliverypartner=models.CharField(max_length=50)
    deliverydate=models.DateField()
    trackid=models.CharField(max_length=50)


    def __str__(self):
        return self.trackid