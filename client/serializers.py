from rest_framework import serializers
from .models import Product_Info, Upload_Prescription, Document, Membership, User_info
#from django.contrib.auth.models import User

class ProductInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Info
        fields = ['name','id','image','price','category','unit','stock']
        owner = serializers.ReadOnlyField(source='owner.username') 

class UploadprescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload_Prescription
        fields = ['created','id','quantity', 'house', 'apartment_number','road_number','mobile_number','delivery_choice','collect_choice']
        owner = serializers.ReadOnlyField(source='owner.username')
         

class UserSerializer(serializers.ModelSerializer):
    #snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Upload_Prescription.objects.all())
    class Meta:
        model = User_info
        fields = [ 'id', 'mobile_number', 'email_address', 'name', 'type', 'road_number', 'apartment_number', 'area', 'house_number', 'total_amount', 'membership']        
        
class UploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document  
        fields = ['upload_file','upload_date'] 

class MembershipSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Membership   
        fields = ['id' , 'type']      
