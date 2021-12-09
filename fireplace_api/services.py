from fireplace_api.models import Fireplace, Command


def add_fire(fire_data: dict):
    fire_data.pop('smartlock')
    Fireplace(**fire_data)\
        .save()


def add_command(fireplace_id: int, data: dict):
    Command(id=fireplace_id, **data).save()
