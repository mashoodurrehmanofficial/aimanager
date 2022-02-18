import enum
from tracemalloc import start
from django.http import JsonResponse
from django.shortcuts import render,redirect,HttpResponse 
from .models import *
from django.views.decorators.csrf import csrf_exempt 
import os,shutil 
from datetime import datetime 
from wsgiref.util import FileWrapper
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .data_file import *
from django.forms.models import model_to_dict

from .views import generateAIProgramDateListing
# Create your views here.



 
def ajaxgenerateAIProgramDateListing(request):
    start_date = request.GET['start_date']
    start_date = datetime.strptime(start_date, '%Y-%m-%d').date() 
    temp_ai_program = AI_Program(start_date= start_date)
    temp_ai_program.save()
    predicted_dates_data = model_to_dict(temp_ai_program)
    predicted_dates_data = generateAIProgramDateListing(temp_ai_program)
    
    temp_ai_program.delete()
    
    print(predicted_dates_data)
    
    return  JsonResponse({'predicted_dates_data':predicted_dates_data}) 