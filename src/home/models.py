from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=300, default='')
    image = models.ImageField(upload_to='restaurant/')

    def __str__(self):
        return self.name
    