# Generated by Django 5.0.1 on 2024-03-21 15:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255, verbose_name="Titre de l'enquête")),
                ('ville', models.CharField(max_length=35, verbose_name='Ville')),
                ('description', models.TextField(verbose_name="Description de l'enquête")),
            ],
        ),
        migrations.CreateModel(
            name='indice_chiffres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=35, verbose_name='Nom')),
                ('code', models.IntegerField(verbose_name='Code')),
                ('contenu_textuel', models.TextField(blank=True, null=True, verbose_name='Contenu textuel')),
                ('contenu_image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Image (ou bien unique, ou bien qui sera à la suite du texte)')),
                ('contenu_audio', models.FileField(blank=True, null=True, upload_to='', verbose_name='Audio')),
                ('contenu_video', models.FileField(blank=True, null=True, upload_to='', verbose_name='Vidéo')),
                ('enquete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.enquete')),
            ],
        ),
    ]
