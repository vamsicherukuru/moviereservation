from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.contrib import auth
from multiselectfield import MultiSelectField
from django.utils import timezone
from datetime import datetime
# Create your models here.



class Product(models.Model):
    name = models.CharField(max_length=100,default='')
    poster = models.ImageField(upload_to = 'movie_posters',blank=True)
   
    description = models.CharField(max_length=1000,default='')
    basic_price = models.IntegerField(default=100)
    
    language_CHOICES = [
    ('Suitcase', 'Suitcase'),
    ('Straws', 'Straws'),
    ('Plates', 'Plates'),
   
    ]
    column_CHOICES = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
   
    ]


    Type = models.CharField(choices = language_CHOICES,max_length=100, default='')
    column_number = models.CharField(choices = column_CHOICES,max_length=100, default='')

   
    def __str__(self):
        return self.name






class UserProfile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    #add_any additional
    Location = models.CharField(max_length=100,default='')
    balance = models.IntegerField(default=5000)
    age = models.IntegerField(default='')
    mobilenumber = models.IntegerField(default='')

    gender = models.CharField(max_length=1,default='M')
    column_CHOICES = [
    ('10,00,000', '10,00,000'),
    ('5,00,000', '5,00,000'),
    ('Below 5 Lakh', 'Below 5 Lakh'),
   
    ]
    income = models.CharField(choices = column_CHOICES,max_length=100, default='')
 

    profilePic = models.ImageField(upload_to = 'profile_pics',blank=True)

    def __str__(self):
        return self.user.username

class Ticket(models.Model):
    movie = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.CharField(max_length=100,null=False)
    income = models.CharField(max_length=100,null=True)
    age = models.CharField(max_length=100,null=False)
    gender = models.CharField(max_length=100,null=False)
    post_date = models.DateTimeField(default=datetime.now)



    def __str__(self):
        return self.movie.name + " - " + self.user +"-" +self.age +" - " +self.gender + " -" + self.movie.column_number
    





class Payment(models.Model):
    
    user = models.CharField(max_length=100,null=False)
    card_number = models.IntegerField(default='')
    cvv = models.IntegerField(default='')
    CardHolder_name =  models.CharField(max_length=100)

    def __str__(self):
        return self.user + " "  + " " + self.CardHolder_name