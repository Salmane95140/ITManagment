from django.urls import path
from it  import views

urlpatterns = [
    path('machines', views.machine_list_view, name='list_machines'),
    path('machine/add', views.machine_add_form, name='add_machine'),
    path('machine/<pk>', views.machine_detail_view, name='detail_machine'),
    path('machine/update/<pk>', views.machine_update_view, name='update_machine'),
    path('machine/delete/<pk>', views.machine_delete_view, name='delete_machine'),
    path('personne', views.personne_list_view, name='list_personnes'),
    path('personne/add', views.personne_add_form, name='add_personne'),
    path('personne/<pk>', views.personne_detail_view, name='detail_personne'),
    path('personne/update/<pk>', views.personne_update_view, name='update_personne'),
    path('personne/delete/<pk>', views.personne_delete_view, name='delete_personne'),
    path('usermachine', views.user_machine_list_view, name="list_usermachine"),
    path('usermachine/add', views.user_machine_add_form, name='add_usermachine'),
    path('usermachine/see/<pk>', views.detail_usermachine, name="detail_usermachine"),
    path('usermachine/update/<pk>', views.user_machine_update_view, name='update_usermachine'),
    path('usermachine/delete/<pk>', views.user_machine_delete_view, name='delete_usermachine'),
    path('maintenancetype', views.TypeMaintenanceListView.as_view(), name='list_typemaintenance'),
    path('maintenancetype/add', views.TypeMaintenanceCreateView.as_view(), name='add_typemaintenance'),
    path('maintenancetype/<pk>', views.TypeMaintenanceDetailView.as_view(), name='detail_typemaintenance'),
]
