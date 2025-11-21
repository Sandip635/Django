from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound, HttpResponseRedirect, Http404 

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


def contact(request):
  return render(request, 'contact.html', {'students': students})



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




## Use of class HttpResponseNotFound 
# This class give if something is not found this class give the message

number = [1,2,3,4,5,6,7,8]
 
def found (request, input_integer):
   for n in number:
     if n == input_integer:
       return HttpResponse("Your typed Number is in the list")
     else:
       return HttpResponseNotFound("Your typed number is not not the list")
     


## Use of class HttpResponseRedirect
# We use url in this class which direct to the specified link

def redirect(request):
  return HttpResponseRedirect('https://www.google.com')


persons = [
    {'id': 1, 'name': 'Ram', 'age': 20, 'skills': 'Python'},
    {'id': 2, 'name': 'Shyam', 'age': 22, 'skills': 'Django'},
    {'id': 3, 'name': 'Hari', 'age': 19, 'skills': 'JavaScript'},
    {'id': 4, 'name': 'Gita', 'age': 21, 'skills': 'React'},
]


def person (request):
  return render(request, 'person.html', {'persons': persons})



def person_display(request, person_id):
   for p in persons:
      selected_person = " "
      if p['id'] == person_id:
          selected_person = p
          break
      return render(request, 'details.html', {'selected_person': selected_person})
  
    





   
