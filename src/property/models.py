from django.db import models
from django.core.validators import RegexValidator
from datetime import datetime, date
# Create your models here.
room_type = (
    ('Non AC Saver (2X)', 'Non AC Saver (2X)'),
    ('Classic (2X)', 'Classic (2X)'),
    ('Delux (3X)', 'Delux (3X)'),
)
class Property(models.Model):
    name = models.CharField(max_length=50, default="Room")
    room_no = models.PositiveIntegerField()
    type = models.CharField(choices=room_type, max_length=100)
    price = models.PositiveIntegerField()
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    area = models.DecimalField(decimal_places=2 , max_digits=10)
    no_of_beds = models.PositiveIntegerField(default= 1)
    image = models.ImageField(upload_to='property/' , null=True)

    def __str__(self):
        return self.name + " " + str(self.room_no)

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category/' , null=True)
    
    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Catogery'
        verbose_name_plural = 'Catogeries'

class Reserve(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?91?\d{9,15}$', message="Phone number must be entered in the format: '+91123456789'. Up to 12 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    no_of_children = models.PositiveSmallIntegerField(default=0)
    no_of_adult = models.PositiveSmallIntegerField(default=0)
    check_in = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    check_out = models.DateTimeField(blank=True)
    

    def __str__(self):
        return self.name
    