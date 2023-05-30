from django.shortcuts import render
from .models import Machine


def machine_list_view(request):
    machines = Machine.objects.all()
    context = {'machines': machines, 'head_title' : "Liste des Equipements"}
    return render(request, 'machine_list.html', context)

def machine_detail_view(request, pk):
    machine = Machine.objects.get(id=pk)
    context = {'machine' : machine, 'head_title' : "Detail Equipement"}
    return render(request, 'machine_detail.html', context)
