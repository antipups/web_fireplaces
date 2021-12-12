from fireplace_api.models import Fireplace, Command


def add_fire(fire_data: dict):
    fire_data.pop('smartlock')
    Fireplace(**fire_data)\
        .save()


def add_command(fireplace_id: int, data: dict):
    if exist_fireplace := Command.objects.filter(id=Fireplace.objects.get(id=fireplace_id)):
        exist_fireplace[0].command = data['command']
        exist_fireplace[0].save()
    else:
        Command(id=Fireplace.objects.get(id=fireplace_id), **data).save()

