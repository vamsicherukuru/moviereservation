from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView
from . import models
from .forms import UserForm,UserProfileForm,TicketForm,PaymentForm
from django.views.decorators.clickjacking import xframe_options_exempt
from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth  import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
import csv
from random import shuffle

# Create your views here.



class Home(ListView):
    template_name = 'home.html'
    model = models.Product
    
    context_object_name = 'movie'
    queryset = models.Product.objects.order_by('-id')





class suitcasesHome(ListView):
    template_name = 'suitcase.html'
    model = models.Product
    
    context_object_name = 'movie'
    queryset = models.Product.objects.order_by('-id').reverse()

class strawHome(ListView):
    template_name = 'strawhome.html'
    model = models.Product
    
    context_object_name = 'movie'
    queryset = models.Product.objects.order_by('-id').reverse()

class platesHome(ListView):
    template_name = 'plateshome.html'
    model = models.Product
    
    context_object_name = 'movie'
    queryset = models.Product.objects.order_by('-id').reverse()

    


   


class product_details(DetailView):
    template_name = 'product_details.html'
    model = models.Product
    
    context_object_name = 'movie'
    
    

class Seat(DetailView):
    template_name = 'seats.html'
    model = models.Product
    
    context_object_name = 'movie'

class TicketBill(ListView):
    template_name = 'ticket.html'
    model = models.Ticket
    
    context_object_name = 'ticket'
    queryset = models.Ticket.objects.order_by('-id')



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('bookings:home'))

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('bookings:home'))
            else:
                return HttpResponse("not active user")
        else:
            return HttpResponse("Invalid Credentials")
        
    else:
        return render(request,'login.html',{})




def RegisterView(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_pic_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_pic_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            profile = profile_pic_form.save(commit=False)
            profile.user = user
            if 'profilePic' in request.FILES:
                profile.profilePic = request.FILES['profilePic']
            profile.save()
            registered = True
        else:
            print(profile_pic_form.errors,user_form.errors)

         
    else:
        user_form = UserForm()
        profile_pic_form = UserProfileForm()

    return render(request,'registration.html',{'user_form':user_form,'profile_pic_form':profile_pic_form
        , 'registered':registered
        })
        





@login_required
def ReservationView(request):
    booked = False
    current_user = request.user.username
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST)
        
        
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user.username
            ticket.age = request.user.userprofile.age
            ticket.income = request.user.userprofile.income
            ticket.gender = request.user.userprofile.gender
            ticket.save()
            booked = True
        else:
            print(ticket_form.errors)

         
    else:
        ticket_form = TicketForm()
        
        

    return render(request,'reservation.html',{'ticket_form':ticket_form
        , 'booked':booked,'cu':current_user
        })
        


   

class profile(ListView):
    template_name = 'profilepage.html'
    model = models.Ticket
    context_object_name = 'booked_ticket'








@login_required
def PaymentView(request):
    payed = False
    current_user = request.user.username
    if request.method == 'POST':
        payment_form = PaymentForm(request.POST)
       
        
        if payment_form.is_valid():
            payment = payment_form.save(commit=False)
           
            payment.user = request.user.username
            payment.save()
            payed = True
        else:
            print(payment_form.errors)

         
    else:
        payment_form = PaymentForm()
        
        

    return render(request,'payment.html',{'payment_form':payment_form
        , 'payed':payed,'cu':current_user
        })






# export Data from Database to excel sheets


def export(request):
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['Product Name','Customer Name','Customer Age','Gender','Product Column','Ordered On','income'])


    for i in models.Ticket.objects.all().values_list('movie__name','user','age','gender','movie__column_number','post_date','income'):
        writer.writerow(i)

    response['Content-Disposition'] = 'attachment; filename="purchase_report.csv"'


    return response
