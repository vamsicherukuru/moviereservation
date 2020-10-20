from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.contrib import auth
from multiselectfield import MultiSelectField
# Create your models here.



class Movie(models.Model):
    name = models.CharField(max_length=100,default='')
    poster = models.ImageField(upload_to = 'movie_posters',blank=True)
    thumbnail = models.ImageField(upload_to = 'thumbnails', null=True)
    director = models.CharField(max_length=100,default='')
    starring = models.CharField(max_length=100,default='')
    genres = models.CharField(max_length=100,default='')
    description = models.CharField(max_length=1000,default='')
    trailer = models.FileField(upload_to='trailer_videos',null=True)
    basic_price = models.IntegerField(default=100)
    
    language_CHOICES = [
    ('Telugu', 'Telugu'),
    ('Hindi', 'Hindi'),
    ('Malayalam', 'Malayalam'),
    ('Tamil', 'Tamil'),
    ('English', 'English'),
    ]

    language = models.CharField(choices = language_CHOICES,max_length=100, default='')
   
    def __str__(self):
        return self.name



class UserProfile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
 
    #add_any additional
    Bio = models.CharField(max_length=100,default='')
    profilePic = models.ImageField(upload_to = 'profile_pics',blank=True)

    def __str__(self):
        return self.user.username

class Ticket(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    user = models.CharField(max_length=100,null=False)

   

    SHOW_CHOICES = [
    ('8:30 AM', '8:30 AM'),
    ('11:30 AM', '11:30 AM'),
    ('2:30 PM', '2:30 PM'),
    ('6:30 PM', '6:30 PM'),
    ('9:30 PM', '9:30 PM'),
    ]

    seat = models.CharField(max_length=100)
    show_timing = models.CharField(choices = SHOW_CHOICES,max_length=100,default = '6:30 PM')
    
    
    
    
    class Meta:
        unique_together = ['movie','seat','show_timing']


    def __str__(self):
        return self.movie.name + " " + "(" + self.seat + ")" + "(" + self.show_timing + ")" + self.user
    


class Theatre(models.Model):
    Theatre_name = models.CharField(max_length=255,default="")



class Payment(models.Model):
    
    user = models.CharField(max_length=100,null=False)
    card_number = models.IntegerField(default='')
    cvv = models.IntegerField(default='')
    CardHolder_name =  models.CharField(max_length=100)
    amount = models.IntegerField(default='')

    def __str__(self):
        return self.user + " "  + str(self.amount) + " " + self.CardHolder_name