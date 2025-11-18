from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (request,a):
  return HttpResponse(f"Hello this is the first url and the dynamic url is {a}")


def show (request):
  return render(request, 'index.html')