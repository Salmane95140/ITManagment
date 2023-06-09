# Generated by Django 4.2.1 on 2023-05-30 15:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=25)),
                ('typeMachine', models.CharField(choices=[('PC', 'PC - Run Windows'), ('Mac', 'Mac Run MacOS'), ('Serveur', 'Simple server to deploy virtual machines'), ('Switch', 'Switch - To maintains and connect servers'), ('Imprimante', 'Imprimante pour impression')], default='PC', max_length=32)),
                ('prix', models.IntegerField()),
                ('dateAchat', models.DateField(default=datetime.datetime(2023, 5, 30, 15, 1, 16, 236943))),
                ('maintenanceDate', models.DateField(default=datetime.datetime(2023, 5, 30, 15, 1, 16, 236943))),
                ('dateFinContrantMaint', models.DateField(default=datetime.datetime(2023, 5, 30, 15, 1, 16, 236943))),
            ],
        ),
    ]
