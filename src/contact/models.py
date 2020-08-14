from django.db import models

# Create your models here.
class ContactDetails(models.Model):
    location = models.CharField(max_length=300, default='')
    email = models.EmailField() 
    phone_no = models.CharField(max_length=15)


    def __str__(self):
        return str(self.id)
    