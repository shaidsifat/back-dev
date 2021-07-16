from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static 
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('home/', views.home1 , name='home'),
    path('product/', views.product , name='product'),
    path('product/<int:pk>/',views.product_detail,name='product_detail'),
    path('post/',views.post,name='product_post'),
    path('',views.api_root),
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns) 