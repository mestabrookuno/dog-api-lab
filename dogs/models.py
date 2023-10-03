from django.db import models

class Breed(models.Model):
    SIZE_CHOICES = [
        ("Tiny", "Tiny"),
        ("Small", "Small"),
        ("Medium", "Medium"),
        ("Large", "Large"),
    ]

    INTEGER_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    name = models.CharField(max_length=30)
    size = models.CharField(max_length=15, choices=SIZE_CHOICES)
    friendliness = models.IntegerField(choices=INTEGER_CHOICES)
    trainability = models.IntegerField(choices=INTEGER_CHOICES)
    sheddingamount = models.IntegerField(choices=INTEGER_CHOICES)
    exerciseneeds = models.IntegerField(choices=INTEGER_CHOICES)

class Dog(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    #breed = models.ForeignKey(Breed, on_delete=models.DO_NOTHING)
    gender = models.CharField(max_length=6)
    color = models.CharField(max_length=14)
    favoritefood = models.CharField(max_length=30)
    favoritetoy = models.CharField(max_length=50)