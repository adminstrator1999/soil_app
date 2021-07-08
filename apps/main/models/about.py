from django.db import models

from main.models import File, BaseModel


class History(BaseModel):
    text = models.TextField()

    class Meta:
        verbose_name_plural = 'Histories'


class HistoryImages(models.Model):
    history = models.ForeignKey(History, on_delete=models.CASCADE)
    image = models.ForeignKey(File, on_delete=models.CASCADE)
