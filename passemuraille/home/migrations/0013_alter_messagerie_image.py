# Generated by Django 5.0.1 on 2024-08-01 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_indices_trouves_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagerie',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
