from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser



class Students(models.Model):
    user = models.CharField(primary_key=True, max_length=20, unique=True)
    name = models.CharField(max_length=20)
   # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$',
                               #  message="Phone number must be entered in the define format")
   # phone = models.CharField(validators=[phone_regex], max_length=12)
    Phone = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    slug = models.SlugField(max_length=200)
    #image = models.ImageField(upload_to='media/students/', null=True, blank=True, height_field='height_field', width_field='width_field')
    #height_field = models.IntegerField(default=0, null=True)
    #width_field = models.IntegerField(default=0, null=True)
    #stream = models.CharField(max_length=50, blank=True)
    stream=models.ForeignKey('Stream',on_delete=models.SET_NULL,null=True,default=1)
    address = models.TextField(max_length=2000, blank=True,null=True)
    registration_number=models.CharField(max_length=200, blank=True,null=True)
    scheme=models.CharField(max_length=200, blank=True,null=True)
    semester=models.ForeignKey('Semester',on_delete=models.SET_NULL,null=True,default=1)
    image = models.ImageField(upload_to='media/students/', blank=True, null=True)
    def __str__(self):
        return str(self.name)

class Stream(models.Model):
    StreamName=models.CharField(max_length=50)

    def __str__(self):
        return str(self.StreamName)

class Semester(models.Model):
    semester=models.CharField(max_length=50)
    def __str__(self):
        return str(self.semester)


  
# Create your models here.