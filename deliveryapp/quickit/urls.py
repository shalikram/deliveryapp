from django.conf.urls import url
from quickit import views
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [


   url('',views.index,name='index'),
   url('admin/',admin.site.urls),
   url('formpage/',views.form_name_view,name='form_name'),
  
  # url('users/',views.users,name='users'),



   ]
