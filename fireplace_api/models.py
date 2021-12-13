from django.db import models


class Fireplace(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    item_model = models.CharField(max_length=32,
                                  verbose_name='Модель')
    ip = models.CharField(max_length=20)
    state = models.SmallIntegerField(default=0)
    length = models.CharField('Длина', max_length=32)
    order_number = models.PositiveIntegerField('№ Заказа')
    seal_number = models.PositiveIntegerField('№ Пломб')
    brand = models.CharField('Бренд', max_length=32)
    version = models.CharField('Версия прошивки', max_length=32)
    send_data = models.DateField('Дата отпр.')
    block = models.BooleanField('Заблокирован', default=False)
    on_or_off = models.BooleanField('Включен',
                                    default=False)
    command = models.SmallIntegerField('То, что возвращается камину',
                                       default=0)


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
