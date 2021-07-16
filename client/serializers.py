from rest_framework import serializers
from .models import info, Snippet 
from django.contrib.auth.models import User

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model =info
        fields = ['client_id','name','unit','image'] 

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id','created', 'name', 'quantity', 'house', 'apartment_number','road_number','mobile_number','delivery_choice']
        owner = serializers.ReadOnlyField(source='owner.username')
         

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = [ 'id','username', 'snippets']        
        
