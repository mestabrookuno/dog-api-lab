from django.shortcuts import render
from django.db import models
from dogs.models import Dog, Breed
from django.http import HttpResponse
from rest_framework import serializers
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

def index(request):
    return HttpResponse("Hello, world!")

def api(request):
    return HttpResponse("You've hit the API endpoint")

class DogSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    age = serializers.IntegerField(default=0)
    breed = serializers.PrimaryKeyRelatedField(queryset=Breed.objects.all())
    gender = serializers.CharField(max_length=6)
    color = serializers.CharField(max_length=14)
    favoritefood = serializers.CharField(max_length=30)
    favoritetoy = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Dog.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.breed = validated_data.get('breed', instance.breed)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.color = validated_data.get('color', instance.color)
        instance.favoritefood = validated_data.get('favoritefood', instance.favoritefood)
        instance.favoritetoy = validated_data.get('favoritetoy', instance.favoritetoy)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
        
class DogViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing dog info. 
    """
    def list(self, request):
        queryset = Dog.objects.all()
        serializer = DogSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Dog.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = DogSerializer(user)
        return Response(serializer.data)

    serializer_class = DogSerializer
    queryset = Dog.objects.all()

class BreedSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    size = serializers.CharField(max_length=15)
    friendliness = serializers.IntegerField(default=3)
    trainability = serializers.IntegerField(default=3)
    sheddingamount = serializers.IntegerField(default=3)
    exerciseneeds = serializers.IntegerField(default=3)
    
    def create(self, validated_data):
        return Breed.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.size = validated_data.get('size')
        instance.friendliness = validated_data.get('friendliness')
        instance.trainability = validated_data.get('trainability')
        instance.sheddingamount = validated_data.get('sheddingamount')
        instance.exerciseneeds = validated_data.get('exerciseneeds')
        instance.save()
        return instance

class BreedViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing breed info. 
    """
    def list(self, request):
        queryset = Breed.objects.all()
        serializer = BreedSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        queryset = Breed.objects.all()
        user = get_object_or_404(queryset, id=pk)
        serializer = BreedSerializer(user)
        return Response(serializer.data)
    
#    def delete(self, request, pk):
#        queryset = Breed.objects.all()
#        user = get_object_or_404(queryset, id=pk)
#        serializer = BreedSerializer(user)
#        return Response(serializer.data)
    
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()