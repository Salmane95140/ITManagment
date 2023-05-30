from django.shortcuts import render
from .models import Machine


def machine_list_view(request):
    machines = Machine.objects.all()
    context = {'machines': machines, 'head_title' : "Liste des machines"}
    return render(request, 'machine_list.html', context)
