from tabnanny import verbose
from django.db import models

# Create your models here.
class Orders(models.Model):
    number = models.IntegerField(verbose_name="Номер заказа", unique=True)
    total_dollar = models.FloatField(verbose_name="Сумма в долларах")
    supply = models.DateField(verbose_name="Срок поставки")
    total_rub = models.FloatField(verbose_name="Сумма в рублях")

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'