from django.db import models

# Create your models here.
class Cow(models.Model):
    text = models.TextField(max_length=100)

    def __str__(self):
        return self.text