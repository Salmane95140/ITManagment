# Generated by Django 4.2.1 on 2023-06-05 15:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('it', '0003_alter_machine_dateachat_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeMaintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('description', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='machine',
            name='dateAchat',
            field=models.DateField(default=datetime.datetime(2023, 6, 5, 15, 42, 36, 194580)),
        ),
        migrations.AlterField(
            model_name='machine',
            name='dateFinContrantMaint',
            field=models.DateField(default=datetime.datetime(2023, 6, 5, 15, 42, 36, 196532)),
        ),
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2023, 6, 5, 15, 42, 36, 196532)),
        ),
        migrations.AlterField(
            model_name='utilisateurmachine',
            name='dateAttribution',
            field=models.DateField(default=datetime.datetime(2023, 6, 5, 15, 42, 36, 196532)),
        ),
    ]
