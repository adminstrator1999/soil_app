from django.db import models

from main.models import BaseModel


class Partner(BaseModel):
    name = models.CharField(max_length=50)
    logo = models.ForeignKey('main.File', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
