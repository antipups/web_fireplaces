from django.db import models


class Fireplace(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    item_model = models.CharField(max_length=32,
                                  verbose_name='Модель')
    length = models.CharField('Длина', max_length=32)
    order_number = models.PositiveIntegerField('№ Заказа')
    seal_number = models.PositiveIntegerField('№ Пломб')
    brand = models.CharField('Бренд', max_length=32)
    version = models.CharField('Версия прошивки', max_length=32)
    send_data = models.DateField('Дата отпр.')


class Logs(models.Model):
    item_id = models.AutoField(primary_key=True)
    id = models.ForeignKey(Fireplace,
                           on_delete=models.CASCADE)
    ip = models.CharField(max_length=20)
    block = models.BooleanField()
    state = models.SmallIntegerField()
    language = models.SmallIntegerField()
    fuel_level = models.IntegerField()
    fire_level = models.IntegerField()
    favorite_mode = models.IntegerField()
    temp_tank = models.IntegerField()
    temp_ten = models.IntegerField()
    temp_burner = models.IntegerField()


class Command(models.Model):
    item_id = models.AutoField(primary_key=True)
    id = models.ForeignKey(Fireplace,
                           on_delete=models.CASCADE)
    command = models.BooleanField()
