from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'bookings'

urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('seats/',views.Seat.as_view(),name='seats'),
    path('seats/<int:pk>',views.Seat.as_view(),name='seats'),
    path('register',views.RegisterView,name='register'),
    path('login',views.user_login,name='user_login'),
    path('logout',views.user_logout,name = 'logout'),
    path('seats/reserve',views.ReservationView,name = 'reserve'),
    path('seats/payment',views.PaymentView,name = 'payment'),
    path('ticket/',views.TicketBill.as_view(),name = 'ticket'),
    path('profile',views.profile.as_view(),name = 'profile'),
]