from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib import messages 
from django.contrib.auth.models import User
from analytics import settings
from django.shortcuts import render, HttpResponse,redirect
from datetime import datetime
import json

# Create your views here.
def index(request):
    return render(request, 'index.html')