from django.db import models
from main.models import BaseModel
from main.models import File


class Employee(BaseModel):
    full_name = models.CharField(max_length=255)
    image = models.ForeignKey(File, on_delete=models.SET_NULL, null=True)
    about = models.TextField()

    def __str__(self):
        return self.full_name
