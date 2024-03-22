from django.db import models

# Create your models here.


class Item(models.Model):

    name = models.CharField(max_length=30)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'


class Client(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='clients')
    date_purchase = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'


class Purchase(models.Model):
    client = models.ForeignKey(Client, related_name='purchases', on_delete=models.CASCADE)
    item = models.ManyToManyField(Item, related_name='purchases', )

    def __str__(self):
        return self.client

