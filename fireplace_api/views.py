import datetime

from django.core.handlers.wsgi import WSGIRequest
from django.forms import ModelForm, DateInput
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView

from fireplace_api import services
from fireplace_api.models import Fireplace


@csrf_exempt
def add_fireplace(request: WSGIRequest, fireplace_id: int):
    services.add_fire(request.POST.dict())
    return HttpResponse("OK")


def add_command(request: WSGIRequest, fireplace_id: int):
    services.add_command(fireplace_id, request.GET.dict())
    return HttpResponse("OK")


class FiresList(ListView):
    model = Fireplace
    template_name = 'firelist.html'
    paginate_by = 10


class FireCreate(CreateView):

    class FireForm(ModelForm):
        class Meta:
            model = Fireplace
            fields = '__all__'
            widgets = {'send_data': DateInput(attrs={'type': 'date'},)}

    template_name = 'firecreate.html'
    form_class = FireForm

    def get_form(self, form_class=None):
        form = super(FireCreate, self).get_form()
        form.fields['send_data'].widget.attrs.update({'value': datetime.date.today()})
        return form

    def get_success_url(self):
        return reverse("create_fireplace")
