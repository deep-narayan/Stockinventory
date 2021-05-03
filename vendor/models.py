from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category_list(models.Model):
	catname=models.CharField(max_length=30)
	desc=models.CharField(max_length=200)
	category_by=models.ForeignKey(User,on_delete=models.CASCADE)
class AllVendor(models.Model):
	vname = models.CharField(max_length=20)
	vcompany=models.CharField(max_length=40)
	vcontact = models.IntegerField()
	vaddress=models.CharField(max_length=100)
	vpincode=models.IntegerField()
	vemail = models.EmailField(max_length=200)
	addedby=models.ForeignKey(User,on_delete=models.CASCADE)
	dated=models.DateTimeField(auto_now_add=True)
class ImportProduct(models.Model):
	name=models.CharField(max_length=100)
	description = models.TextField(max_length=250)
	title = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=9, decimal_places=4)
	created_at = models.DateTimeField(auto_now_add=True)
	brand = models.CharField(max_length=100)
	model = models.CharField(max_length=100)
	pro_category=models.ForeignKey(Category_list,on_delete=models.CASCADE)
	pro_vendor=models.ForeignKey(AllVendor,on_delete=models.CASCADE)
	qty=models.IntegerField()
	rate=models.DecimalField(max_digits=9, decimal_places=4)
	total_price=models.DecimalField(max_digits=20, decimal_places=4)
	ImportingUser=models.ForeignKey(User,on_delete=models.CASCADE)

class Store(models.Model):
	name=models.CharField(max_length=100)
	description = models.TextField(max_length=250)
	title = models.CharField(max_length=100)
	selling_price = models.DecimalField(max_digits=9, decimal_places=4)
	cost_price=models.DecimalField(max_digits=9, decimal_places=4)
	brand = models.CharField(max_length=100)
	model = models.CharField(max_length=100)
	pro_category=models.ForeignKey(Category_list,on_delete=models.CASCADE)
	qty=models.IntegerField()
	ImportingUser=models.ForeignKey(User,on_delete=models.CASCADE)

class Customer_Detail(models.Model):
	c_name=models.CharField(max_length=100)
	c_mobile=models.CharField(max_length=12)
	c_mobile_optional=models.CharField(max_length=12)
	c_address=models.CharField(max_length=200)
	added_by=models.ForeignKey(User,on_delete=models.CASCADE)
class Sell(models.Model):
	name=models.CharField(max_length=100)
	description = models.TextField(max_length=250)
	title = models.CharField(max_length=100)
	totalprice = models.DecimalField(max_digits=9, decimal_places=4)
	brand = models.CharField(max_length=100)
	model = models.CharField(max_length=100)
	pro_category=models.ForeignKey(Category_list,on_delete=models.CASCADE)
	qty=models.IntegerField()
	ExportingUser=models.ForeignKey(User,on_delete=models.CASCADE)
	rate=models.DecimalField(max_digits=9, decimal_places=4)
	created_at = models.DateTimeField(auto_now_add=True)
	customer_detail=models.ForeignKey(Customer_Detail,on_delete=models.CASCADE)