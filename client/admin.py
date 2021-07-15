

# Register your models here.
from django.contrib import admin
from .models import info, Snippet, Upload 
# Register your models here.
admin.site.register(info)
admin.site.register(Snippet)
admin.site.register(Upload)

