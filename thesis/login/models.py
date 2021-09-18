from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class thesis(models.Model):
    TitleId = models.BigIntegerField(primary_key=True)
    Student_Name = models.CharField(max_length=100)
    time = models.TimeField(default=timezone.now)
    date = models.DateTimeField(default=timezone.now)
    Speciality = models.CharField(max_length=100)
    ExaminorId = models.ForeignKey(User, on_delete=models.CASCADE)
    filepass = models.CharField(max_length=100)
    Remarks = models.CharField(max_length=1000)
    Thesis_Type = models.BooleanField(default=0)
    Status = models.BooleanField(default=0)
    file = models.FileField()

class Bank(models.Model):
    ExaminorId = models.ForeignKey(User, on_delete=models.CASCADE)
    IFSC = models.CharField(max_length=20)
    Name_place = models.CharField(max_length=100)
    account_no = models.CharField(max_length=20)
    name = models.CharField(max_length=100)