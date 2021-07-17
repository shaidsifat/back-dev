from rest_framework import serializers
from .models import Product_Info, Upload_Prescription  
from django.contrib.auth.models import User

class ProductInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Info
        fields = ['id','name','image','price','category','unit','stock']
        owner = serializers.ReadOnlyField(source='owner.username') 

class UploadprescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload_Prescription
        fields = ['id','created', 'name', 'quantity', 'house', 'apartment_number','road_number','mobile_number','delivery_choice']
        owner = serializers.ReadOnlyField(source='owner.username')
         

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Upload_Prescription.objects.all())

    class Meta:
        model = User
        fields = [ 'id','username', 'snippets']        
        
