from django.urls import path
from first_app import views

urlpatterns = [
    # Define your URL patterns here
    path('hello/<int:a>', views.home ),
    path('show', views.show),
    path('index/', views.index),
    path('index1/<int:z>/', views.index1)


]
