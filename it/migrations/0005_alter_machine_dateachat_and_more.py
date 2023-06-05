# Generated by Django 4.2.1 on 2023-06-05 15:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('it', '0004_typemaintenance_alter_machine_dateachat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='dateAchat',
            field=models.DateField(default=datetime.datetime(2023, 6, 5, 15, 43, 41, 449955)),
        ),
        migrations.AlterField(
            model_name='machine',
            name='dateFinContrantMaint',
            field=models.DateField(default=datetime.datetime(2023, 6, 5, 15, 43, 41, 449955)),
        ),
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2023, 6, 5, 15, 43, 41, 449955)),
        ),
        migrations.AlterField(
            model_name='utilisateurmachine',
            name='dateAttribution',
            field=models.DateField(default=datetime.datetime(2023, 6, 5, 15, 43, 41, 449955)),
        ),
        migrations.CreateModel(
            name='MaintenancePreventive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime(2023, 6, 5, 15, 43, 41, 449955))),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='it.machine')),
                ('personne', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='it.personne')),
                ('type_maintenance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='it.typemaintenance')),
            ],
        ),
    ]