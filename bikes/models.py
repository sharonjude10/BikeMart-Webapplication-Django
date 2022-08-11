from django.db import models
from unicodedata import category, name


# Create your models here.
class Destination(models.Model):
    name= models.CharField(max_length=100)
    img= models.ImageField(upload_to='pics')
    desc= models.TextField()
    rate= models.IntegerField()
    category=models.CharField(max_length=100)
    




    

# Create your models here.
