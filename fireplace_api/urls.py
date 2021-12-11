from django.urls import path
from fireplace_api import views


urlpatterns = [
    path('', views.FiresList.as_view(), name='firelist'),
    path('create_fireplace', views.FireCreate.as_view(), name='create_fireplace'),
    path('id<int:fireplace_id>/log', views.add_fireplace),
    path('id<int:fireplace_id>/command', views.add_command)
]
