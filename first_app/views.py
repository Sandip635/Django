from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound

## Here, django.http and django.shortcuts are python module ( file or package containing code)
## Inside HttpResponse and HttpResponseNotFound are class defined inside django.http module

# Create your views here.
# Dyanmic url is make by defining paramenter in views function 
def home (request,a):
  return HttpResponse(f"Hello this is the first url and the dynamic url is {a}")

# Rendering a html page which is done by using render subclass
def show (request):
  return render(request, 'index.html')

# Creating a list of dictionary and make the dynamic url there 
students = [
    {
        "id": 0,
        "name": "Sandip",
        "skills": ["Python", "Django", "HTML", "CSS"],
        "education": "Bachelor's in Computer Science"
    },

    {
        "id": 1,
        "name": "Aashish",
        "skills": ["JavaScript", "React", "Node.js"],
        "education": "Bachelor's in Information Technology"
    },

    {
        "id": 2,
        "name": "Rohan",
        "skills": ["C", "C++", "Data Structures"],
        "education": "Diploma in Software Engineering"
    },

    {
        "id": 3,
        "name": "Rana",
        "skills": ["SQL", "Power BI", "Excel"],
        "education": "MBA in Business Analytics"
    },
]

# Here, index view gives all the dictionary of list 
# we make anchor tag inside index view through we make the implementation of DYNAMIC URL
def index(request):
  html = " "
  for student in students:
    s = student
    html += f'''
      <div> 
      <a href = '/index1/{s['id']}/'> 
       <p> {s['name']} </p> 
      </a>
       <p>{s['skills']} </p>
       <p> {s['education']} </p>
      </div>
      <hr/>
    '''
  return HttpResponse(html)



def index1 (request, z):
  
  for student in students:
      if student['id']==z :
       single = student
       break
     
    
  html = f'''
            <p> {single['name']} </p>
       <p>{single['skills']} </p>
       <p> {single['education']} </p>
       '''
  return HttpResponse(html)

