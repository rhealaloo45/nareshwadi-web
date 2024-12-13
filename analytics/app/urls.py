from django.contrib import admin
from django.urls import path
from app import views

from django.views.decorators.csrf import csrf_exempt
from . import views

from . import views
urlpatterns = [
    path('',csrf_exempt(views.index), name='app'),
    # path('home',views.home, name='home'),
]