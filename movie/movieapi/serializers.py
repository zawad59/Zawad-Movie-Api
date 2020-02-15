from rest_framework import serializers

from .models import Details
from .models import Comments

#Two serializers to display stored data from two models 

class Details_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Details
        fields = ["m_id","Title","Year","Rated","Released","Runtime","Genre","Director","Writer","Actors",
        "Plot","Language","Country","Awards","Poster","Ratings","Metascore","imdbRating","imdbVotes",
        "imdbID","Type","DVD","BoxOffice","Production","Website","Response"]
 


class Comments_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comments
        fields = ('comment_id', 'm_id', 'comments')

