from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from fireplace_api import services


@csrf_exempt
def add_fireplace(request: WSGIRequest, fireplace_id: int):
    services.add_fire(request.POST.dict())
    return HttpResponse("OK")


def add_command(request: WSGIRequest, fireplace_id: int):
    services.add_command(fireplace_id, request.GET.dict())
    return HttpResponse("OK")
