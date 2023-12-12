from django.urls import path,include
from . import views
app_name='bankingapp'
urlpatterns = [
    path('',views.home,name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/',views.login,name='login'),
    path('services/',views.services,name='services'),
    path('logout/',views.logout,name='logout'),
    path('details',views.details,name='details'),
    path('transfer',views.money,name='transfer'),
    path('registration_success',views.registration_success,name='registration_success'),
]