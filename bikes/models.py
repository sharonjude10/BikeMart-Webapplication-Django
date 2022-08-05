from django.db import models
from unicodedata import name


# Create your models here.
class Destination(models.Model):
    name= models.CharField(max_length=100)
    img= models.ImageField(upload_to='pics')
    desc= models.TextField()
    rate= models.IntegerField()




    

# Create your models here.
