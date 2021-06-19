from django.db import models

# Create your models here.


class Shoes(models.Model):
    
    name= models.CharField(max_length=100)
    price = models.FloatField()
    size=models.IntegerField()
    img = models.ImageField(upload_to='pics')
    rate= models.IntegerField()
    promotion=models.BooleanField()
    description=models.TextField()

    

   
        