from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('loginpage/' , views.login_page),
    path('register/',views.register),
    path('newuser/',views.newuser),
    path('logoutpage/',views.logout_page),
]