from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class MealSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meal
        fields = ('id','title','description','no_of_ratings','avg_ratings')


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id','meal','user','stars')
        
        
class UserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)

    class Meta :
        model = User
        fields = ('id','username','password')    
        