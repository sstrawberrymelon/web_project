from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'


class Client(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    date_purchase = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'