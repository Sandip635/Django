from django.db import models

# Create your models here
class Student(models.Model):
  name = models.CharField(max_length=100)
  age = models.IntegerField(default=10)
  location = models.TextField()
  
  def __str__(self):
    return self.name
  
  