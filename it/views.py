from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Machine, Personne, UtilisateurMachine, TypeMaintenance, MaintenancePreventive
from it.forms import AddMachineForm, MachineForm, PersonneForm, UtilisateurMachineForm, TypeMaintenanceForm, MaintenanceForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.core.mail import send_mail

def index(request):
    #context = {'head_title': "Accueil"}
    return render(request, 'accueil.html')

def seloger(request):
    return render(request, 'login.html')

def login_view(request):
    if request.method == 'POST':

        nom = request.POST["email"]
        mot_de_passe = request.POST["passe"]
        user = authenticate(username=nom, password=mot_de_passe)
        if user is not None:
            context = {'active': 'active', 'head_title' : "Dashboard"}

            return render(request, 'dashboard.html', context)
        else:
            return render(request, 'error_login.html')

# fonction liste des machines ou equipements
def machine_list_view(request):
    #recupurer l'ensemble des machines
    machines = Machine.objects.all()
    #mettre dans le context l'ensemble des machine et le texte a affiche
    context = {'machines': machines, 'head_title' : "Liste des Equipements"}
    return render(request, 'machine_list.html', context)

# les details de chaque machine avec comme parametre pk qui l'id de la machine
def machine_detail_view(request, pk):
    #recupurer la machine correspondant au pk en parametre
    machine = Machine.objects.get(id=pk)
    context = {'machine' : machine, 'head_title' : "Detail Equipement"}
    return render(request, 'machine_detail.html', context)

#fonction de creation d'une machine
def machine_add_form(request) :
    # verifie si la raquete est de type POST
    if request.method == "POST":
        # creer le formulaire et ajouter les donnees dans le formulaire apartir du request:
        form = AddMachineForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            #creation d'une machine
            machine = Machine(nom = form.cleaned_data['nom'], typeMachine=form.cleaned_data['typeMachine'],  prix= form.cleaned_data['prix'],
            dateAchat = form.cleaned_data['dateAchat'], maintenanceDate = form.cleaned_data['maintenanceDate'], dateFinContrantMaint = form.cleaned_data['dateFinContrantMaint'])
            # sauvegarde d'une machine dans la base de donnees
            machine.save()
            #retour vers la liste des machines
            return HttpResponseRedirect("/machines")

    # si la requete est de type GET ou autre creer un formulaire vide
    else:
        form = AddMachineForm()

    return render(request, "add_machine.html", {"form": form})

#modification machine
def machine_update_view(request, pk):
    context ={'head_title' : "Modification Equipement"}
    #recherche la machine si elle est trouve retourne l'objet sinon renvoi not found
    obj = get_object_or_404(Machine, id = pk)
    #rempli le formulaire
    form = MachineForm(request.POST or None, instance = obj)
    #verifie si le formulaire est valide
    if form.is_valid():
        #modification
        machine = form.save()
        context['machine'] = machine
        #retour a detail machine
        return render(request, 'machine_detail.html', context)
    context["form"] = form

    return render(request, "update_machine.html", context)

#suppression machine
def machine_delete_view(request, pk):
    #recherche la machine si elle est trouve retourne l'objet sinon renvoi not found
    machine = get_object_or_404(Machine, id=pk)
    #supprimer la machine
    machine.delete()
    #message status suppression
    messages.success(request, "Suppression reussi.")
    #retour vers liste machine
    return HttpResponseRedirect("/machines")

def personne_list_view(request):
    personnes = Personne.objects.all()
    context = {'personnes': personnes, 'head_title' : "Liste des Employes"}
    return render(request, 'personne_list.html', context)

def personne_add_form(request) :
    if request.method == "POST":
        form = PersonneForm(request.POST)
        if form.is_valid():
            personne = Personne(prenom = form.cleaned_data['prenom'], nom=form.cleaned_data['nom'], email=form.cleaned_data['email'], poste= form.cleaned_data['poste'])
            personne.save()
            messages.success(request, "Ajout reussi.")

            return HttpResponseRedirect("/personne")
    else:
        form = PersonneForm()

    return render(request, "add_personne.html", {"form": form})

def personne_detail_view(request, pk):
    personne = Personne.objects.get(id=pk)
    context = {'personne' : personne, 'head_title' : "Detail Employe"}
    return render(request, 'personne_detail.html', context)

def personne_update_view(request, pk):
    context ={}
    obj = get_object_or_404(Personne, id = pk)
    form = PersonneForm(request.POST or None, instance = obj)
    if form.is_valid():
        personne = form.save()
        context['personne'] = personne
        return render(request, 'personne_detail.html', context)
    context["form"] = form

    return render(request, "update_personne.html", context)

def personne_delete_view(request, pk):
    personne = get_object_or_404(Personne, id=pk)
    personne.delete()
    messages.success(request, "Suppression reussi.")
    return HttpResponseRedirect("/personne")

def user_machine_list_view(request):
    user_machines = UtilisateurMachine.objects.all()
    context = {'user_machines': user_machines, 'head_title' : "Liste des utilisateurs et machines"}

    return render(request, 'list_utilisateur_machine.html', context)

def user_machine_add_form(request) :
    if request.method == "POST":
        form = UtilisateurMachineForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/usermachine")
    else:
        form = UtilisateurMachineForm()
    return render(request, "add_utilisateur_machine.html", {"form": form})

def detail_usermachine(request, pk):
    user_machine = UtilisateurMachine.objects.get(pk=pk)
    context = {'user_machine' : user_machine, 'head_title' : "Detail Equipement Employe"}
    return render(request, 'user_machine_detail.html', context)

def user_machine_update_view(request, pk):
    context ={}
    obj = get_object_or_404(UtilisateurMachine, id = pk)
    form = UtilisateurMachineForm(request.POST or None, instance = obj)
    if form.is_valid():
        user_machine = form.save()
        context['user_machine'] = user_machine
        return render(request, 'user_machine_detail.html', context)
    context["form"] = form

    return render(request, "update_user_machine.html", context)

def user_machine_delete_view(request, pk):
    user_machine = get_object_or_404(UtilisateurMachine, id=pk)
    user_machine.delete()
    messages.success(request, "Suppression reussi.")
    return HttpResponseRedirect("/usermachine")
#list des types de maintenance avec des vue fondees sur la class
class TypeMaintenanceListView(ListView):
    #model a lister
    model = TypeMaintenance
    #le template a utiliser
    template_name = 'type_maintenance_list.html'
    #nom variable utiliser au niveau du template
    context_object_name = 'type_maintenances'

class TypeMaintenanceCreateView(CreateView):
    model = TypeMaintenance
    form_class = TypeMaintenanceForm
    template_name = 'type_maintenance_form.html'
    #si la creation est reussi retourner a la liste des types de maintenance
    success_url = reverse_lazy('list_typemaintenance')

    #controle la validite du formulaire d'ajout
    def form_valid(self, form):
        messages.success(self.request, "Ajout reussi.")
        return super(TypeMaintenanceCreateView,self).form_valid(form)

class TypeMaintenanceDetailView(DetailView):
    model = TypeMaintenance
    template_name = 'type_maintenance_detail.html'
    context_object_name = 'type_maintenance'

class TypeMaintenanceUpdateView(UpdateView):
    model = TypeMaintenance
    form_class = TypeMaintenanceForm
    template_name = 'type_maintenance_form.html'
    success_url = reverse_lazy('list_typemaintenance')

    def form_valid(self, form):
        messages.success(self.request, "Modification reussi.")
        return super(TypeMaintenanceUpdateView,self).form_valid(form)

class TypeMaintenanceDeleteView(DeleteView):
    model = TypeMaintenance
    context_object_name = 'typemaintenance'
    template_name = 'suppression_typemaintenance_form.html'
    success_url = reverse_lazy('list_typemaintenance')

    def form_valid(self, form):
        messages.success(self.request, "Suppression reussi.")
        return super(TypeMaintenanceDeleteView,self).form_valid(form)

class MaintenancePreventiveListView(ListView):
    model = MaintenancePreventive
    template_name = 'maintenance_list.html'
    context_object_name = 'maintenances'

class MaintenancePreventiveCreateView(CreateView):
    model = MaintenancePreventive
    form_class = MaintenanceForm
    template_name = 'maintenance_form.html'
    success_url = reverse_lazy('list_maintenance')

    def form_valid(self, form):
        messages.success(self.request, "Ajout reussi.")
        return super(MaintenancePreventiveCreateView,self).form_valid(form)

class MaintenancePreventiveDetailView(DetailView):
    model = MaintenancePreventive
    template_name = 'maintenance_detail.html'
    context_object_name = 'maintenance'

class MaintenancePreventiveUpdateView(UpdateView):
    model = MaintenancePreventive
    form_class = MaintenanceForm
    template_name = 'maintenance_form.html'
    success_url = reverse_lazy('list_maintenance')

    def form_valid(self, form):
        messages.success(self.request, "Modification reussi.")
        return super(MaintenancePreventiveUpdateView,self).form_valid(form)

class MaintenancePreventiveDeleteView(DeleteView):
    model = MaintenancePreventive
    context_object_name = 'maintenance'
    template_name = 'suppression_maintenance_form.html'
    success_url = reverse_lazy('list_maintenance')

    def form_valid(self, form):
        messages.success(self.request, "Suppression reussi.")
        return super(MaintenancePreventiveDeleteView,self).form_valid(form)

def envoi_email_maintenance(request, pk):
    maintenance = MaintenancePreventive.objects.get(pk=pk)
    #recupuration email destinataire
    email = maintenance.personne.email
    sujet = "Maintenance Equipement"
    msg = ("La %s de votre Equipement %s sera faite le %s")%(maintenance.type_maintenance.nom, maintenance.machine.nom, maintenance.date)
    #envoi de email de maintenance
    send_mail(
    sujet,
    msg,
    "itmanagement@it.com",
    [email],
    fail_silently=False,
    )

    return HttpResponseRedirect("/maintenance")
