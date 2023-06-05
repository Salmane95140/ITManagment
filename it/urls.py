from django.urls import path
from it  import views

urlpatterns = [
    path('machines', views.machine_list_view, name='list_machines'),
    path('machine/add', views.machine_add_form, name='add_machine'),
    path('machine/<pk>', views.machine_detail_view, name='detail_machine'),
    path('machine/update/<pk>', views.machine_update_view, name='update_machine'),
    path('machine/delete/<pk>', views.machine_delete_view, name='delete_machine'),
    path('personne', views.personne_list_view, name='list_personnes'),
]
