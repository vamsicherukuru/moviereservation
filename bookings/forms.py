from django import forms
from django.contrib.auth.models import User
from . import models
from bookings.models import (UserProfile,Ticket,Payment)
from django.forms import ModelForm
from . import views

class UserProfileForm(forms.ModelForm):
    Location = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Location'}),label="search")
    age = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Age'}),label="search")
    gender = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Gender'}),label="search")
    mobilenumber = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Mobile number'}),label="search")

    class Meta():
        model = UserProfile
        fields = ('profilePic','Location','age','gender','mobilenumber','income')
class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}),label="search")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),label="search")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email-id'}),label="search")
    class Meta():
        model = User
        fields = ('username','password','email')



class TicketForm(forms.ModelForm):
   
  
#     user = forms.CharField(initial="",widget=forms.TextInput(attrs={'readonly':'readonly'})
# )
    


    class Meta():
        model = Ticket
        fields = '__all__'
        exclude = ('user','age','gender','post_date','income')

class PaymentForm(forms.ModelForm):
   
    class Meta():
        model = Payment
        fields = '__all__'
        exclude = ('user',)