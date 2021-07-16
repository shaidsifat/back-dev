from django.db import models
from django.conf import settings
# Create your models here.

class info(models.Model):

   
    client_id = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/post_image',blank=True)
    price = models.CharField(max_length=12)
    category = models.CharField(max_length=100)
    unit = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    quantity = models.IntegerField()
    house = models.CharField(max_length=20)
    apartment_number = models.CharField(max_length=10, blank = True)
    road_number = models.CharField(max_length=10, blank=True)
    mobile_number=models.CharField(max_length=10, blank=True)


    Delivery_options = [
        ('REGULAR', 'R'),
        ('EXPRESS', 'E'),
    ]

    delivery_choice = models.CharField(max_length=30, blank=True, null=True, choices=Delivery_options)
    
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE, blank=True)

    class Meta:
        ordering = ['created'] 

class Upload(models.Model):
    upload_file = models.FileField()    
    upload_date = models.DateTimeField(auto_now_add =True)        
    owner = models.ForeignKey('auth.User', related_name='upload', on_delete=models.CASCADE, blank=True)
    def __unicode__(self):
        return self.name


