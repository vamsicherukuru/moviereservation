from django import forms
from django.contrib.auth.models import User
from . import models
from bookings.models import (UserProfile,Ticket,Payment)
from django.forms import ModelForm
from . import views

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('profilePic',)
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password')



class TicketForm(forms.ModelForm):
   
  
    BOOL_CHOICES = [
    ('A1', 'A1'),
    ('A2', 'A2'),
    ('A3', 'A3'),
    ('A4', 'A4'),
    ('A5', 'A5'),]      
    
   
#     user = forms.CharField(initial="",widget=forms.TextInput(attrs={'readonly':'readonly'})
# )
    seat= forms.MultipleChoiceField( choices = BOOL_CHOICES,widget=forms.CheckboxSelectMultiple())

    def clean_seat(self):
        value = self.cleaned_data['seat']
        if len(value) > 3:
            raise forms.ValidationError("You can't select more than 3 items.")
        return value
   
    class Meta():
        model = Ticket
        fields = '__all__'
        exclude = ('user',)

class PaymentForm(forms.ModelForm):
   
    class Meta():
        model = Payment
        fields = '__all__'
        exclude = ('user',)