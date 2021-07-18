from django.db import models
from django.conf import settings
# Create your models here.

class Product_Info(models.Model):

    #client_id = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='media/post_image',blank=True)
    price = models.CharField(max_length=12)
    category = models.CharField(max_length=100)
    #sub_category = models.CharField(max_length=100)
    unit = models.CharField(max_length=10) 
    stock = models.IntegerField()
    
    owner = models.ForeignKey('auth.User', related_name='products', on_delete=models.CASCADE, blank=True)

    class Meta:
        ordering = ['name']

    #def __str__(self):
    #    return self.name

class Upload_Prescription(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True) 
    #name = models.CharField(max_length=100, blank=True, default='')
    quantity = models.IntegerField()
    house = models.CharField(max_length=20)
    apartment_number = models.CharField(max_length=10, blank = True)
    road_number = models.CharField(max_length=10, blank=True)
    mobile_number=models.CharField(max_length=10, blank=True)
    area = models.CharField(max_length=10, blank=True)


    Delivery_options = [
        ('REGULAR', 'R'),
        ('EXPRESS', 'E'),
    ]

    delivery_choice = models.CharField(max_length=30, blank=True, null=True, choices=Delivery_options)

    Collect_options = [
        ('Collect from store','CS'),
        ('Delivery','D'),
    ]
    
    collect_choice = models.CharField(max_length=30, blank=True, null=True, choices=Collect_options)

    owner = models.ForeignKey('auth.User', related_name='upload_pres', on_delete=models.CASCADE, blank=True)

    class Meta:
        ordering = ['created'] 

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True) 


class Membership(models.Model):
    id = models.AutoField(primary_key=True)
    type_options = [
        ('REGULAR_USER', 'R'),
        ('MEMBER', 'M'),
    ]
    type = models.CharField(max_length=30, blank=True, null=True, choices=type_options, unique= True) 


    owner = models.ForeignKey('auth.User', related_name='mem_details', on_delete=models.CASCADE, blank=True)
    class Meta:
        ordering = ['id']
    

class User_info(models.Model):
    id = models.AutoField(primary_key=True) 
    mobile_number = models.CharField(max_length=10, blank=True)
    email_address = models.EmailField(max_length=254) 
    name = models.CharField(max_length=100, blank=True, default='')
    type_options = [
        ('REGULAR_USER', 'R'),
        ('MEMBER', 'M'),
    ]
    type = models.CharField(max_length=30, blank=True, null=True, choices=type_options) 
    road_number = models.CharField(max_length=10, blank=True) 
    apartment_number = models.CharField(max_length=10, blank=True)
    area = models.CharField(max_length=10, blank=True)
    house_number = models.CharField(max_length=10, blank=True) 
    total_amount = models.CharField(max_length=10, blank=True)
    membership = models.ForeignKey(Membership, to_field='type', on_delete=models.CASCADE)

    owner = models.ForeignKey('auth.User', related_name='users', on_delete=models.CASCADE, blank=True)
    class Meta:
        ordering = ['id']


    
    
