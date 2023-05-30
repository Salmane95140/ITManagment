from django.urls import path
from it  import views

urlpatterns = [
    path('machines', views.machine_list_view, name='list_machines'),
    path('machine/<pk>', views.machine_detail_view, name='detail_machine'),
]
