import datetime

from django.core.handlers.wsgi import WSGIRequest
from django.forms import ModelForm, DateInput
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView

from fireplace_api import services
from fireplace_api.models import Fireplace, Command


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

    def get_context_data(self, *, object_list=None, **kwargs):
        contex_data = super(FiresList, self).get_context_data()
        contex_data['fires_on'] = Command.objects.filter(command=True).count()
        contex_data['fires_off'] = Command.objects.filter(command=False).count()
        return contex_data


class FireForm(ModelForm):
    class Meta:
        model = Fireplace
        fields = '__all__'
        widgets = {'send_data': DateInput(attrs={'type': 'date'},)}


class FireCreate(CreateView):

    template_name = 'firecreate.html'
    form_class = FireForm

    def get_form(self, form_class=None):
        form = super(FireCreate, self).get_form()
        form.fields['send_data'].widget.attrs.update({'value': datetime.date.today()})
        return form

    def get_success_url(self):
        return reverse("create_fireplace")


class FireUpdate(UpdateView):

    form_class = FireForm
    template_name = 'firecreate.html'

    def get_object(self, queryset=None):
        return Fireplace.objects.get(id=self.request.resolver_match.kwargs['fireplace_id'])

    def get_success_url(self):
        return reverse("firelist")

