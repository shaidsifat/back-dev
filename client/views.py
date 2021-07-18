from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response 
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import ProductInfoSerializer, UploadprescriptionSerializer, UserSerializer, UploadSerializer, MembershipSerializer 
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser, FileUploadParser
from rest_framework.views import APIView 
from rest_framework.reverse import reverse
from . import views 
from rest_framework.decorators import api_view 
from rest_framework import status, generics 
#from django.contrib.auth.models import User 
from django.shortcuts import render, redirect 
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Product_Info, Upload_Prescription, Document, User_info, Membership 
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth.decorators import login_required
#from .forms import UploadForm
from .forms import UploadForm, DocumentForm 
from .functions import handle_uploaded_file

def home1(request):
    list = Product_Info.objects.all()
    context ={

          'Product_Info':list
    }
    return render(request,'home.html',context)

'''
@api_view(['POST'])
def post(self, request, format=None):
        serializer = ProductInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def product(request):
   if request.method == 'GET':
   	  list = Product_Info.objects.all()
   	  serializer = ProductInfoSerializer(list,many=True)
   	  return Response(serializer.data)


   elif request.method == 'POST':
        serializer = ProductInfoSerializer(data=request.data)
        if serializer.is_valid():
        	 serializer.save()
        	 return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)	

@api_view(['GET','PUT','DELETE'])
def product_detail(request,pk):
    try:
        list = Product_Info.objects.get(id=pk)
    
    except Product.DoesNotExist:
        return Response(status= status.HTTP_400_BAD_REQUEST)
    
    except Product.DoesNotExist:
        return Response(status= status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        serializer = ProductInfoSerializer(list)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductInfoSerializer(list,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''

class ProductUploadList(generics.ListCreateAPIView):
    queryset = Upload_Prescription.objects.all()
    serializer_class = UploadprescriptionSerializer
    def perform_create(self, serializer):
       serializer.save(owner=self.request.user)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]   


class ProductUploadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Upload_Prescription.objects.all()
    serializer_class = UploadprescriptionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

class ProductList(generics.ListCreateAPIView):
    queryset = Product_Info.objects.all()
    serializer_class = ProductInfoSerializer
    def perform_create(self, serializer):
       serializer.save(owner=self.request.user)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]   


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product_Info.objects.all()
    serializer_class = ProductInfoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'uploads': reverse('upload-list', request=request, format=format)
    })

@api_view(['POST'])
def post_data(request):
    serializer = UploadprescriptionSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'products': reverse('product-list', request=request, format=format)
    })

@api_view(['POST'])
def post_data(request):
    serializer = ProductInfoSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)




class UserList(generics.ListCreateAPIView):
    queryset = User_info.objects.all()
    serializer_class = UserSerializer
    def perform_create(self, serializer):
       serializer.save(owner=self.request.user)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] 
    
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User_info.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly] 


class MembershipList(generics.ListCreateAPIView):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
    def perform_create(self, serializer):
       serializer.save(owner=self.request.user)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] 
    
class MembershipDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]     

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'user': reverse('user-list', request=request, format=format)
    })

@api_view(['POST'])
def post_data(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'membership': reverse('membership-list', request=request, format=format)
    })

@api_view(['POST'])
def post_data(request):
    serializer = MembershipSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


'''

class MembershipList(generics.ListAPIView):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
    def perform_create(self, serializer):
       serializer.save(owner=self.request.user)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] 
    
class MembershipDetail(generics.RetrieveAPIView):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly] 

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'membership': reverse('membership-list', request=request, format=format)
    })

@api_view(['POST'])
def post_data(request):
    serializer = MembershipSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

'''

def index(request):  
    if request.method == 'POST':  
        uform = UploadForm(request.POST, request.FILES)  
        if uform.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            return HttpResponse("File uploaded successfuly")  
    else:  
        uform = UploadForm()  
        return render(request,"index.html",{'form':uform})     

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })
