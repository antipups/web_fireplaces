from django.urls import path
from fireplace_api import views


urlpatterns = [
    path('', views.FiresList.as_view(), name='firelist'),
    path('create_fireplace', views.FireCreate.as_view(), name='create_fireplace'),
    path('fireplace/<int:fireplace_id>', views.FireUpdate.as_view(), name='update_fireplace'),
    path('search', views.FiresList.as_view(), name='filter_search'),
    path('log', views.add_fireplace),
    path('id<int:fireplace_id>/command', views.get_command)
]
