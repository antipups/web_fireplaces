import datetime

from fireplace_api.models import Fireplace, Logs
from global_config import AMOUNT_MINUTES_FOR_OFF


def add_logs(fire_data: dict):
    if 'smartlock' in fire_data:
        fire_data.pop('smartlock')

    fireplace = Fireplace.objects.get(id=fire_data['id'])
    fireplace.state = fire_data['state']

    fireplace.on_or_off = (datetime.datetime.now() + datetime.timedelta(hours=3, minutes=AMOUNT_MINUTES_FOR_OFF))

    fireplace.save()

    fire_data['id'] = fireplace
    Logs(**fire_data)\
        .save()


def get_command(fireplace_id: int) -> int:
    fireplace = Fireplace.objects.get(id=fireplace_id)
    logs_block = Logs.objects.filter(id=fireplace).last().block

    if not logs_block and fireplace.block:
        return 2
    elif logs_block and not fireplace.block:
        return 1
    else:
        return 0
