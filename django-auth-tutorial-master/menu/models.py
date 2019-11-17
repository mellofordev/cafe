from django.db import models


from order.models import Purchase

# Create your models here.
class Menu(models.Model):
    product=models.ManyToManyField(Purchase,blank=True)

    total=models.IntegerField(default=0)
    def __str__(self):
        return self.product


