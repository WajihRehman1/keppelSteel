from django.db import models


# Create your models here.
from django.urls import reverse


class services(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    picture = models.ImageField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("basic_app:index")


class svcItems(models.Model):
    title=models.CharField(max_length=15)
    services = models.ForeignKey(services,on_delete=models.CASCADE,related_name="myService")
    description = models.TextField()
    picture = models.ImageField()

    def get_absolute_url(self):
        return reverse("basic_app:index")


