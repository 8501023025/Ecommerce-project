from django.db import models


# Create your models here.
class products(models.Model):
    name = models.CharField(max_length=20)
    price=models.IntegerField()
    image=models.ImageField(upload_to='images')
    slug=models.CharField(max_length=30,unique=True)
    description=models.TextField(blank=True,null=True)
    
    
    def __str__(self):
        return self.name