from fireplace_api.models import Fireplace, Logs


def add_logs(fire_data: dict):
    fire_data.pop('smartlock')

    fireplace = Fireplace.objects.get(id=fire_data['id'])
    fireplace.state = fire_data['state']
    fireplace.save()

    fire_data['id'] = fireplace
    Logs(**fire_data)\
        .save()


def add_command(fireplace_id: int, data: dict):
    fireplace = Fireplace.objects.get(id=fireplace_id)
    fireplace.command = data['command']
    fireplace.save()
