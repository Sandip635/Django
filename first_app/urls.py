from django.urls import path
from first_app import views

urlpatterns = [
    # Define your URL patterns here
    path('hello/<int:a>', views.home ),
    path('show', views.show),
    path('contact', views.contact, name="contact"),
    path('index/', views.index, name="index"),
    path('index1/<int:z>/', views.index1),
    path('found/<int:input_integer>', views.found),
    path('redirect/', views.redirect, name ="redirect"),
    path('person/', views.person, name="person"),
    path('person/<int:person_id>/', views.person_display, name="person_display"),



]
