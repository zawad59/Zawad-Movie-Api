from django.contrib import admin
from django.urls import path, include
from movieapi import views

#Calling appropriate urls and respective functions to render 

urlpatterns = [
     path('admin/', admin.site.urls),
     path('', include('movieapi.urls')),
     path('comments_by_id/', views.idm),
     path('home/', views.home),
     path('info/',  views.new_page,  name="my_function"),
     path('comments_list/',  views.query, name = "query"),
     path('filter_movie/', views.title_filter),
     path('result_filter/', views.filter, name = "filter")
 ]
