from django.db import models

from main.models import BaseModel


class GalleryType(models.Model):
    title = models.CharField(max_length=255)


class Gallery(BaseModel):
    image = models.ForeignKey('main.File', on_delete=models.CASCADE, null=True, blank=True, related_name='image')
    video = models.ForeignKey('main.File', on_delete=models.CASCADE, null=True, blank=True, related_name='video')
    type = models.ForeignKey(GalleryType, on_delete=models.SET_NULL, null=True, blank=True)
