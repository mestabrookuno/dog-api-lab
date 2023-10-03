from django.shortcuts import render
from django.db import models
from dogs.models import Dog, Breed
from django.http import HttpResponse
from rest_framework import serializers
from rest_framework import viewsets

def index(request):
    return HttpResponse("Hello, world!")

def api(request):
    return HttpResponse("You've hit the API endpoint")

class DogSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    age = serializers.IntegerField(default=0)
   # breed = models.ForeignKey(Breed, on_delete=models.DO_NOTHING)
    gender = serializers.CharField(max_length=6)
    color = serializers.CharField(max_length=14)
    favoritefood = serializers.CharField(max_length=30)
    favoritetoy = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Dog.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.color = validated_data.get('color', instance.color)
        instance.favoritefood = validated_data.get('favoritefood', instance.favoritefood)
        instance.favoritetoy = validated_data.get('favoritetoy', instance.favoritetoy)
        return instance

class DogViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing dog info. 
    """
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
        instance.name = validated_data.get('name', instance.name)
        instance.size = validated_data.get('size', instance.size)
        instance.friendliness = validated_data.get('friendliness', instance.friendliness)
        instance.trainability = validated_data.get('trainability', instance.trainability)
        instance.sheddingamount = validated_data.get('sheddingamount', instance.sheddingamount)
        instance.exerciseneeds = validated_data.get('exerciseneeds', instance.exerciseneeds)
        return instance

class BreedViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing breed info. 
    """
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()