from django.db import models
from main.models import BaseModel, DeleteMixin
from main.models import File


class Role(BaseModel, DeleteMixin):
    role = models.CharField(max_length=100)
    degree = models.IntegerField()

    def __str__(self):
        return self.role


class Employee(BaseModel):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=17)
    birth_date = models.DateField()
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    image = models.ForeignKey(File, on_delete=models.SET_NULL, null=True)
    about = models.TextField()
    position = models.IntegerField(null=True)

    def __str__(self):
        return self.full_name
