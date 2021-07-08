from django.db import models
from main.models import BaseModel


class Contact(BaseModel):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.full_name
