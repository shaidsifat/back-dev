

# Register your models here.
from django.contrib import admin
from .models import Product_Info, Upload_Prescription, Document, User_info, Membership
# Register your models here.
admin.site.register(Product_Info)
admin.site.register(Upload_Prescription)
admin.site.register(Document)
admin.site.register(User_info)
admin.site.register(Membership)


