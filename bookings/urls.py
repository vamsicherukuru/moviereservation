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
    path('paymentgateway/',views.ReservationView,name = 'reserve'),
    path('seats/payment',views.PaymentView,name = 'payment'),
    path('ticket/',views.TicketBill.as_view(),name = 'ticket'),
    path('profile',views.profile.as_view(),name = 'profile'),
    path('suitcases',views.suitcasesHome.as_view(),name='suitcases'),
    path('straws',views.strawHome.as_view(),name='straw'),

    path('plates',views.platesHome.as_view(),name='plates'),

    path('product/<int:pk>',views.product_details.as_view(),name='product_details'),
    path('export',views.export,name='export'),

]