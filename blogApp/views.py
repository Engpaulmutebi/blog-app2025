from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request,month):
  message = None;

  if month == 'jan':
    message = "happy new year dear"
  elif month == 'feb':
    message = 'I love you sweet' 
  else:
    message = 'not supported'   



  return HttpResponse(message)
