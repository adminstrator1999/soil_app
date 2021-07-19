from django.db import models

from main.models import BaseModel


class Laboratory(BaseModel):
    name = models.CharField(max_length=255)
    body = models.TextField()

    class Meta:
        verbose_name_plural = 'Laboratories'

    def __str__(self):
        return self.name


class LaboratoryImage(models.Model):
    laboratory = models.ForeignKey(Laboratory, on_delete=models.CASCADE)
    image = models.ForeignKey('main.File', on_delete=models.CASCADE)
