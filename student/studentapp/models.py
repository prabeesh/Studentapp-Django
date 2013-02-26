from django.db import models

class student(models.Model):
	name = models.CharField(max_length=30)
	sex = models.CharField(max_length=30)
	age = models.CharField(max_length=30)
	mark = models.CharField(max_length=30)
# Create your models here.
