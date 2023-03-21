from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    date = models.DateTimeField()
    text = models.CharField(max_length=1000)

    def __str__(self):
        return self.title