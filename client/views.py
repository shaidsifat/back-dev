from .models import info
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import InfoSerializer
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response 
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer 
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser, FileUploadParser
from rest_framework.views import APIView 
from rest_framework.reverse import reverse
from . import views 
from rest_framework.decorators import api_view 
from rest_framework import status, generics 
from django.contrib.auth.models import User 
from django.shortcuts import render 
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Upload 
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth.decorators import login_required
#from .forms import UploadForm
from .forms import StudentForm 
from .functions import handle_uploaded_file

def home1(request):
    list = info.objects.all()
    context ={

          'infos':list
    }
    return render(request,'home.html',context)

def post(self, request, format=None):
        serializer = InfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def product(request):
   if request.method == 'GET':
   	  list = info.objects.all()
   	  serializer = InfoSerializer(list,many=True)
   	  return Response(serializer.data)


   elif request.method == 'POST':
        serializer = InfoSerializer(data=request.data)
        if serializer.is_valid():
        	 serializer.save()
        	 return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)	

@api_view(['GET','PUT','DELETE'])
def product_detail(request,pk):
    try:
        list = info.objects.get(id=pk)

    except Product.DoesNotExist:
        return Response(status= status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = InfoSerializer(list)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = InfoSerializer(list,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    def perform_create(self, serializer):
       serializer.save(owner=self.request.user)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]   


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })

@api_view(['POST'])
def post_data(request):
    serializer = SnippetSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def index(request):  
    if request.method == 'POST':  
        student = StudentForm(request.POST, request.FILES)  
        if student.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            return HttpResponse("File uploaded successfuly")  
    else:  
        student = StudentForm()  
        return render(request,"index.html",{'form':student})     


