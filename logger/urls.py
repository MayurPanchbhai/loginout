from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('loginpage/' , views.login_page),
    path('login/', views.login)
]