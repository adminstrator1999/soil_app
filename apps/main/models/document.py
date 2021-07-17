from django.db import models

from main.models import BaseModel


class Document(BaseModel):
    name = models.CharField(max_length=255)
    link1 = models.URLField(null=True, blank=True)
    link2 = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class DocumentImages(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    image = models.ForeignKey('main.File', on_delete=models.CASCADE)
