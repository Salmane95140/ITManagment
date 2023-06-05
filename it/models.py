from django.db import models
from datetime import datetime

class Machine(models.Model):

    TYPE=(
        ('PC', ('PC - Run Windows')),
        ('Mac', ('Mac Run MacOS')),
        ('Serveur', ('Simple server to deploy virtual machines')),
        ('Switch', ('Switch - To maintains and connect servers')),
        ('Imprimante', ('Imprimante pour impression'))
    )
    id = models.AutoField(primary_key= True, editable = False)
    nom = models.CharField(max_length=25)
    typeMachine = models.CharField(max_length=32, choices=TYPE, default='PC')
    prix = models.IntegerField()
    dateAchat = models.DateField(default=datetime.now())
    maintenanceDate = models.DateField(default=datetime.now())
    dateFinContrantMaint = models.DateField(default=datetime.now())

    def __str__(self):
        return self.nom

class Personne(models.Model):
    id = models.AutoField(primary_key= True, editable = False)
    prenom = models.CharField(max_length=20)
    nom = models.CharField(max_length=20)
    poste = models.CharField(max_length=20)

    def __str__(self):
        return '%s %s'%(self.nom, self.prenom)

class UtilisateurMachine(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    personne = models.ForeignKey(Personne, on_delete=models.CASCADE)
    dateAttribution = models.DateField(default= datetime.now())

    class Meta:
        unique_together = ["machine", "personne"]

    def __str__(self):
        return '%s - %s'%(self.personne , self.machine )
