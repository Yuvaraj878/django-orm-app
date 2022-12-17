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

# Create your models here.
