from django.urls import path
from fireplace_api import views


urlpatterns = [
    path('id<int:fireplace_id>/log', views.add_fireplace),
    path('id<int:fireplace_id>/command', views.add_command)
]
