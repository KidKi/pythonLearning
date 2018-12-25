from django.db import models

# Create your models here.

class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    studentName = models.CharField(max_length=32)
    score = models.CharField(max_length=32)
