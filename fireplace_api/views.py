import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.handlers.wsgi import WSGIRequest
from django.forms import ModelForm, DateInput
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView

from fireplace_api import services
from fireplace_api.models import Fireplace, Logs
from json import loads


@csrf_exempt
def add_fireplace(request: WSGIRequest):
    try:
        services.add_logs(loads(request.body.decode()))
    except Exception as e:
        return HttpResponse(status=400,)
    else:
        return HttpResponse('')


def get_command(request: WSGIRequest, fireplace_id: int):
    return JsonResponse({'command': services.get_command(fireplace_id=fireplace_id)})


class FiresList(LoginRequiredMixin, ListView):
    model = Fireplace
    template_name = 'firelist.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super(FiresList, self).get_queryset()
        url_args: dict = self.request.GET.dict()

        if ('search_type' in url_args and 'search_value' in url_args) and url_args['search_value']:    # поиск с фильтрами
            queryset = Fireplace.objects.filter(**{url_args['search_type']: url_args['search_value']})
            # self.request.session.update(url_args)
        # else:
        #     self.request

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        contex_data = super(FiresList, self).get_context_data()
        current_time = datetime.datetime.now().replace(tzinfo=datetime.timezone.utc)
        contex_data['fires_on'] = Fireplace.objects.filter(on_or_off__gt=current_time).count()
        contex_data['fires_off'] = Fireplace.objects.filter(on_or_off__lt=current_time).count()
        contex_data['amount_errors'] = Fireplace.objects.filter(state__in=[212, 222, 223, 224, 225, 226, 227])\
            .count()
        return contex_data


class FireForm(ModelForm):
    class Meta:
        model = Fireplace
        fields = '__all__'
        exclude = ['command']
        widgets = {'send_data': DateInput(attrs={'type': 'date'},)}


class FireCreate(LoginRequiredMixin, CreateView):

    template_name = 'firecreate.html'
    form_class = FireForm

    def get_form(self, form_class=None):
        form = super(FireCreate, self).get_form()
        form.fields['send_data'].widget.attrs.update({'value': datetime.date.today()})
        return form

    def get_context_data(self, **kwargs):
        context = super(FireCreate, self).get_context_data()
        context['create'] = True
        return context

    def get_success_url(self):
        return reverse("create_fireplace")


class FireUpdate(LoginRequiredMixin, UpdateView):

    form_class = FireForm
    template_name = 'firecreate.html'

    def get_object(self, queryset=None):
        return Fireplace.objects.get(id=self.request.resolver_match.kwargs['fireplace_id'])
    
    def get_context_data(self, **kwargs):
        context = super(FireUpdate, self).get_context_data()
        context['logs'] = Logs.objects.filter(id=Fireplace.objects.get(id=self.request.resolver_match.kwargs['fireplace_id']))
        return context

    def get_success_url(self):
        return reverse("firelist")
