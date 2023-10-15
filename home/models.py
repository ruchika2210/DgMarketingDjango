from django.db import models

# Create your models here.

class Contact(models.Model):
    firstName=models.CharField(max_length=122)
    lastName= models.CharField(max_length=122)
    City=models.CharField(max_length=122)
    Zip=models.CharField(max_length=122)

def __str__(self):
    return self.firstName

