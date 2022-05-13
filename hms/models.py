import email
from time import time
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
import datetime

# Create your models here.

class Contact_us(models.Model):
    name = models.CharField(max_length=20)
    emailid = models.EmailField()
    contactnumber = models.IntegerField()
    subjecttocontact = models.TextField()
    desc = models.TextField()
    dateofcontact = models.DateTimeField()

    def __str__(self):
        return self.subjecttocontact

class UserProfile(models.Model):
    userz = models.OneToOneField(User, on_delete=CASCADE)
    contactnumber = models.IntegerField()
    dateofbirth = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()

    def __str__(self):
        return self.userz.first_name


class Appointment(models.Model):
    appointmentid = models.IntegerField(default=0)
    appointmentdesc = models.CharField(max_length=1000,default="nothing here")
    of_whom = models.CharField(max_length=50)
    appointmentdate = models.DateField()
    appointmenttime = models.TimeField()
    active = models.BooleanField()
    with_whom = models.CharField(max_length=50)

    def __str__(self):
        return self.of_whom


class Document(models.Model):
    user = models.ForeignKey(User,on_delete=CASCADE)
    docexp = models.CharField(max_length=30)
    file = models.FileField(upload_to="documents/")

    def __str__(self) :
        return self.docexp

class UpdateNew(models.Model):
    title = models.CharField(max_length=100)
    messageis = models.CharField(max_length=1000)
    messageby = models.CharField(max_length=100)
    messageon = models.DateField()

    def __str__(self) -> str:
        return self.title

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    experience = models.IntegerField()
    specialization = models.CharField(max_length=300)
    docdesc = models.CharField(max_length=1000,default="No info available")
    start_time = models.TimeField()
    end_time = models.TimeField()
    current_date = models.DateField()
    current_time = models.TimeField()

    def __str__(self)->str:
        return self.name
