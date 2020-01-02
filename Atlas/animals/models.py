from django.db import models

class Food(models.Model):
    type = models.CharField(max_length=100)
    def __str__(self):
        return self.type


class Animal(models.Model):
    name = models.CharField(max_length=150)
    eat = models.ForeignKey(Food, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=2083)
    objects: models.Manager()




# Create your models here.
