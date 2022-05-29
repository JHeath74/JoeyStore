from django.db import models


# Create your models here.

class Inventory(models.Model):

    def __str__(self):
        return self.Item_Name

    Item_Name = models.CharField(max_length=250)
    Item_Price = models.IntegerField(max_length=25)
    Item_Description = models.TextField(max_length=5000)
    Item_Ingredients = models.TextField(max_length=5000)
    Item_Amount_in_Inventory = models.IntegerField(max_length=200)
    Item_Images = models.ImageField(upload_to='images/')
