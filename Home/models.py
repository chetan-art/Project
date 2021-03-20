from django.db import models

# Create your models here.
class AddStudent(models.Model): # In model we define the feilds of form and its type.
    Name = models.CharField(max_length = 100)
    Father_Name = models.CharField(max_length = 100)
    Mobile = models.BigIntegerField()
    Class = models.CharField(max_length = 100)
    Status = models.CharField(max_length = 100)
