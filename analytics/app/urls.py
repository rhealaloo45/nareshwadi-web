from django.contrib import admin
from django.urls import path
from app import views

from django.views.decorators.csrf import csrf_exempt
from . import views

from . import views
urlpatterns = [
    path('',csrf_exempt(views.index), name='app'),
    path('disease',views.disease, name='disease'),
    path('milk', views.predict_milk_production, name="predict_milk"),
    path("result/", views.result, name="result"),
    # path('predict/', views.milk_yield_prediction, name='milk_yield_prediction'),
]