from django.shortcuts import render
from rest_framework import viewsets , permissions
from .models import *
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import request
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny , IsAuthenticated , IsAdminUser , IsAuthenticatedOrReadOnly


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [AllowAny,]
    

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    
    @action(methods=['post'], detail=True)
    def rate_meal(self, request, pk=None):
        if 'stars' in request.data:
            meal = Meal.objects.get(id=pk)
            user = request.user
            username = request.data['username']
            #user = User.objects.get(username=username)
            stars = request.data['stars']
            
            try:
                # Update if rating already exists
                rating = Rating.objects.get(user=user.id, meal=meal.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                
                json = {
                    'message': 'Meal Rate Update',
                    'result': serializer.data,
                }
                return Response(json, status=status.HTTP_200_OK)
            
            except Rating.DoesNotExist:
                # Create a new rating if it doesn't exist
                rating = Rating.objects.create(stars=stars, meal=meal, user=user)
                serializer = RatingSerializer(rating, many=False)
                
                json = {
                    'message': 'Meal Rate Created',
                    'result': serializer.data,
                }
                return Response(json, status=status.HTTP_200_OK)
            
        else:
            # Return error if stars field is not provided
            json = {
                'message': 'Stars not provided',
            }
            return Response(json, status=status.HTTP_400_BAD_REQUEST)

              

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer    
    
    authentication_classes = [TokenAuthentication , ]
    permission_classes = [IsAuthenticated, ]
    
    def update(self, request, *args, **kwargs):
        response = {
            'message': 'Invalid way to create or update '
            }

        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def create(self, request, *args, **kwargs):
        response = {
            'message': 'Invalid way to create or update '
            }

        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    