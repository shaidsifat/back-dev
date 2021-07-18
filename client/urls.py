from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static 
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('home/', views.home1 , name='home'),
    path('product/', views.ProductList.as_view()),
    path('product/<int:pk>/',views.ProductDetail.as_view()),
    path('',views.api_root),
    path('uploadlist/', views.ProductUploadList.as_view()),
    path('uploadlist/<int:pk>/', views.ProductUploadDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('fileup/', views.model_form_upload , name='fileup'),
    path('membershiplist/', views.MembershipList.as_view()),
    path('membershiplist/<int:pk>/', views.MembershipDetail.as_view()),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

urlpatterns = format_suffix_patterns(urlpatterns)

#path('post/',views.post,name='product_post')