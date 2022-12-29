from django.db import models


class MenuItems(models.Model):

    item_name = models.CharField(max_length=255)
    item_description = models.CharField(max_length=255)
    item_price = models.DecimalField(max_digits=6, decimal_places=2)
    item_inventory = models.SmallIntegerField()






 


