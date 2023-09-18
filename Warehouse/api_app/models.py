from django.db import models


class Order(models.Model):
    # Опис поля моделі Order
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory_count = models.PositiveIntegerField()

    def __str__(self):
        return self.title
