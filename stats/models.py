from django.db import models


class Stats(models.Model):
    text = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Stats'

    def __str__(self):
        return self.text
