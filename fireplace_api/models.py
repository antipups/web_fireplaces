from django.db import models


class Fireplace(models.Model):
    item_id = models.AutoField(primary_key=True)
    id = models.PositiveIntegerField()
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
    id = models.PositiveIntegerField(primary_key=False)
    command = models.BooleanField()
