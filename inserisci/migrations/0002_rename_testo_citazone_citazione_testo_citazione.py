# Generated by Django 5.1.2 on 2024-12-03 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inserisci', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='citazione',
            old_name='testo_citazone',
            new_name='testo_citazione',
        ),
    ]
