from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128, default="")
    # states = models.ManyToManyField('State', through='Site')
    def __str__(self) :
        return self.name

class State(models.Model):
    name = models.CharField(max_length=200, default="")
    # category is set to null
    # regions = models.ForeignKey('Region', on_delete=models.SET_NULL, null=True)
    # categories = models.ManyToManyField('Category', through='Site')
    def __str__(self) :
        return self.name

class Iso(models.Model):
    name = models.CharField(max_length=128, default="")
    def __str__(self) :
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=200, default="")
    # iso is set to null
    # isoes = models.ForeignKey('Iso', on_delete=models.SET_NULL, null=True)
    def __str__(self) :
        return self.name

class Site(models.Model):
    name = models.CharField(max_length=300, null=True)
    year = models.IntegerField(null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    description = models.TextField(max_length=300, null=True)
    justification = models.TextField(null=True)
    area_hectares = models.FloatField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    region = models.ForeignKey("Region", on_delete=models.CASCADE, null=True)
    iso = models.ForeignKey("Iso", on_delete=models.CASCADE, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)

    def __str__(self) :
        return self.name

