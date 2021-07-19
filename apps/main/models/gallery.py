from django.db import models

from main.models import BaseModel


class GalleryType(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Gallery(BaseModel):
    image = models.ForeignKey('main.File', on_delete=models.CASCADE, null=True, blank=True, related_name='image')
    video = models.ForeignKey('main.File', on_delete=models.CASCADE, null=True, blank=True, related_name='video')
    type = models.ForeignKey(GalleryType, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Galleries'

    def __str__(self):
        return self.type.title
