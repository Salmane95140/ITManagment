from django import forms
from django.core.exceptions import ValidationError
from it.models import Machine

class DateInput(forms.DateInput):
    input_type = 'date'
class AddMachineForm(forms.Form):
    TYPE=(
        ('PC', ('PC - Run Windows')),
        ('Mac', ('Mac Run MacOS')),
        ('Serveur', ('Simple server to deploy virtual machines')),
        ('Switch', ('Switch - To maintains and connect servers')),
        ('Imprimante', ('Imprimante pour impression'))
    )
    nom = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required = True, label = 'Nom de la machine')
    typeMachine = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-select'}),choices=TYPE)
    prix = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    dateAchat = forms.DateField(widget=DateInput(attrs={'class': 'form-control'}), label='Date Achat')
    maintenanceDate = forms.DateField(widget=DateInput(attrs={'class': 'form-control'}), label='Maintenance Date')
    dateFinContrantMaint = forms.DateField(widget=DateInput(attrs={'class': 'form-control'}), label='Date fin contrat')

    # def clean_nom(self):
    #     data = self.cleaned_data["nom"]
    #     if len(data) != 6:
    #         raise ValidationError((" Erreur de format pour le champ nom"))
    #     return data

class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = [
             "nom",
             "typeMachine",
             "prix",
             "dateAchat",
             "maintenanceDate",
             "dateFinContrantMaint"
             ]
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'typeMachine': forms.Select(attrs={'class': 'form-select'}),
            'prix': forms.NumberInput(attrs={'class': 'form-control'}),
            'dateAchat': DateInput(attrs={'class': 'form-control'}),
            'maintenanceDate': DateInput(attrs={'class': 'form-control'}),
            'dateFinContrantMaint': DateInput(attrs={'class': 'form-control'}),
        }
