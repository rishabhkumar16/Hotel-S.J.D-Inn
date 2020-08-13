from django.db import models

# Create your models here.
class Staff(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(default=0)
    emp_id = models.CharField(max_length=50)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='staff/')

    def __str__(self):
        return self.name + " " +self.emp_id
    