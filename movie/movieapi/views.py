from rest_framework import viewsets
from django.shortcuts import render
from .serializers import Details_Serializer
from .models import Details
from django.http import JsonResponse
from rest_framework import viewsets
from django.forms.models import model_to_dict
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import urllib
import requests
import json
from urllib.request import urlopen
import urllib.request
from django.http import HttpResponse
import pymysql
from django.db import connection
from django.db.utils import OperationalError
from .serializers import Comments_Serializer
from .models import Comments
from django.template.loader import render_to_string
from django.core import serializers
from django.db import connection

#Contains functions to render responses to templates and connector between models and serializer
url_omdb = ('http://www.omdbapi.com/?t=')
api_key = '48782d39'

#functions to view all data contained in two models

class View_Details(viewsets.ModelViewSet):
    queryset = Details.objects.all()
    serializer_class = Details_Serializer

class View_Comments(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = Comments_Serializer  

def home(request):
    return render(request, 'home.html')
    
def idm(request):
    return render(request, 'comments_by_id.html')
 
def title_filter(request):
    return render(request,'filter_movie.html')

#Function to filter comments posted for a particular movie by passing ID

def query(self):
    movie_id = self.GET["comments"]
    with connection.cursor() as cursor:
        cursor.execute("Select comments from movieapi_comments WHERE m_id_id = %s",[movie_id])
        row = cursor.fetchall()
        comm = []
    for r in row:
        comm.append(r[0])
    str = "movie id " + movie_id + "'s comments : "
    return JsonResponse({str : comm})

#Function to filter IMDB info of a particular movie by passing its title    

def filter(self):
    movie_title = self.GET["filter"]
    with connection.cursor() as cursor:
        cursor.execute("Select imdbRating,imdbVotes from movieapi_details WHERE Title like %s",[movie_title])
        row = cursor.fetchall()
        it = iter(row) 
        res_dct = dict(zip(it, it)) 
        info = []
    for r in row:
        info.append(r[0])
        info.append(r[1])
    str = "IMDB Rating followed by Total IMDB Votes" + " for " + movie_title
    return JsonResponse({str : info})

#Function to fetch JsonResponse from Omdbapi when passed movie title and then store information to the model

def new_page(request):
    show_data = request.GET['title']
    for i in range(len(show_data)):
        if(show_data[i]==' '):
           show_data = show_data.replace(' ','+')
    final_url = url_omdb + show_data + '&apikey=' + api_key 
    response = urllib.request.urlopen(final_url)
    data = json.loads(response.read())
    
    #return 
    d = Details(Title = data["Title"], Year = data["Year"], Rated = data["Rated"],
    Released = data["Released"], Runtime = data["Runtime"], Genre = data["Genre"],
    Director = data["Director"], Writer = data["Writer"], Actors = data["Actors"],
    Plot = data["Plot"], Language = data["Language"], Country = data["Country"],
    Awards = data["Awards"], Poster = data["Poster"], Ratings = data["Ratings"],
    Metascore = data["Metascore"], imdbRating = data["imdbRating"], imdbVotes = data["imdbVotes"],
    imdbID = data["imdbID"], Type = data["Type"], DVD = data["DVD"], BoxOffice = data["BoxOffice"],
    Production = data["Production"], Website = data["Website"], Response = data["Response"])
    d.save()
    return (JsonResponse(data))