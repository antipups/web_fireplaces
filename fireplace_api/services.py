from fireplace_api.models import Fireplace, Logs


def add_logs(fire_data: dict):
    if 'smartlock' in fire_data:
        fire_data.pop('smartlock')

    fireplace = Fireplace.objects.get(id=fire_data['id'])
    fireplace.state = fire_data['state']
    fireplace.block = fire_data['block']
    fireplace.save()

    fire_data['id'] = fireplace
    Logs(**fire_data)\
        .save()


def get_command(fireplace_id: int) -> int:
    fireplace = Fireplace.objects.get(id=fireplace_id)
    return fireplace.command
