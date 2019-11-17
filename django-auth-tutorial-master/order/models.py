from django.db import models

# Create your models here.
class Purchase(models.Model):


    pname=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    dis=models.CharField(max_length=200,default="")
    slug = models.SlugField(default="")

    def __str__(self):
        return self.pname

