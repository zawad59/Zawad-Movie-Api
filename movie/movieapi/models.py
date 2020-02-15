from django.db import models

from django.core.validators import validate_comma_separated_integer_list

#Declaring two models and respective fields, Comments class gets has m_id from Details as foreign key so that only IDs from the stored movies can be commented 

class Details(models.Model):
    m_id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=1000, unique=True)
    Year = models.CharField(max_length=1000)
    Rated = models.CharField(max_length=1000)
    Released = models.CharField(max_length=1000)
    Runtime = models.CharField(max_length=1000)
    Genre = models.CharField(max_length=1000)
    Director = models.CharField(max_length=1000)
    Writer = models.CharField(max_length=1000)
    Actors = models.CharField(max_length=1000)
    Plot = models.CharField(max_length=1000)
    Language = models.CharField(max_length=1000)
    Country = models.CharField(max_length=1000)
    Awards = models.CharField(max_length=1000)
    Poster = models.CharField(max_length=1000)
    Ratings = models.CharField(max_length=1000)
    Metascore = models.IntegerField()
    imdbRating = models.FloatField(max_length=1000)
    imdbVotes= models.CharField(validators=[validate_comma_separated_integer_list],max_length=200)
    imdbID = models.CharField(max_length=1000)
    Type = models.CharField(max_length=1000)
    DVD = models.CharField(max_length=1000)
    BoxOffice = models.CharField(max_length=1000)
    Production= models.CharField(max_length=1000)
    Website = models.CharField(max_length=1000)
    Response = models.CharField(max_length=1000)
    
class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    m_id = models.ForeignKey(Details, on_delete = models.CASCADE)
    comments = models.CharField(max_length=1000)
