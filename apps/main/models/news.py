from .base_model import BaseModel
from django.db import models


class News(BaseModel):
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=500)
    body = models.TextField()
    view_count = models.IntegerField(default=0)
    video = models.URLField(null=True)

    class Meta:
        verbose_name_plural = "News"

    def __str__(self):
        return self.title


class NewsImage(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    image = models.ForeignKey('main.File', on_delete=models.CASCADE)
