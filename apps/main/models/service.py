from django.db import models
from main.models import BaseModel


class Service(BaseModel):
    name = models.CharField(max_length=255)
    about = models.TextField()

    def __str__(self):
        return self.name


class ServiceImages(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    image = models.ForeignKey('main.File', on_delete=models.CASCADE)


class Function(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title
