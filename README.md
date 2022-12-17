# Django ORM Web Application

## AIM
To develop a Django application to store and retrieve data from a database using Object Relational Mapping(ORM).

## Entity Relationship Diagram
![WhatsApp Image 2022-12-17 at 18 45 49](https://user-images.githubusercontent.com/118622554/208243804-d4bb13a7-d6bd-458f-b553-d8884a109989.jpg)

## DESIGN STEPS

### STEP 1:
Create a new Django project using "django-admin startproject",get into the project terminal and use
"python3 manage.py startapp" command.
### STEP 2:
Define a model for the  BankAccountmembership in the models.py.Allow host access and add the app
name under installed apps in settings.py

### STEP 3:
Register the models with the Django admin site. In admin.py under app folder,register the models
with Django admin site.
### STEP 4:
Run the python manage.py makemigrations and python manage.py migrate commands to create the
necessary database tables for the BankAccountmembership model.Run the Server using "python3
manage.py runserver 0:80" command.


## PROGRAM
#IN models.py:-

from django.db import models
from django.contrib import admin
#Create your model here.
class BankAccountMember(models.Model):
    account_number = models.CharField(max_length=16,primary_key=True)
    name =models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    phone_number = models.IntegerField()

class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('account_number','name','age','email','phone_number')

#IN admin.py:-

from django.contrib import admin
from .models import BankAccountMember,BankAccountAdmin

admin.site.register(BankAccountMember,BankAccountAdmin)


## OUTPUT
![WhatsApp Image 2022-12-17 at 18 46 33](https://user-images.githubusercontent.com/118622554/208243839-d17b781e-a644-4cbd-8d57-45b0c4c8d5bd.jpg)


## RESULT
Successfully developed a Django application to store and retrieve data from a database using Object
Relational Mapping(ORM).
