# Generated by Django 4.2.1 on 2023-06-05 12:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('it', '0002_personne_alter_machine_dateachat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='dateAchat',
            field=models.DateField(default=datetime.datetime(2023, 6, 5, 12, 14, 52, 12616)),
        ),
        migrations.AlterField(
            model_name='machine',
            name='dateFinContrantMaint',
            field=models.DateField(default=datetime.datetime(2023, 6, 5, 12, 14, 52, 12616)),
        ),
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2023, 6, 5, 12, 14, 52, 12616)),
        ),
        migrations.CreateModel(
            name='UtilisateurMachine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateAttribution', models.DateField(default=datetime.datetime(2023, 6, 5, 12, 14, 52, 13614))),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='it.machine')),
                ('personne', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='it.personne')),
            ],
            options={
                'unique_together': {('machine', 'personne')},
            },
        ),
    ]
