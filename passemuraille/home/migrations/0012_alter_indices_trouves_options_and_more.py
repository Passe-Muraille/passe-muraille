# Generated by Django 5.0.1 on 2024-08-01 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_messagerie_date_envoie'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='indices_trouves',
            options={'verbose_name': 'Indice trouvé', 'verbose_name_plural': 'Indices trouvés'},
        ),
        migrations.AlterModelOptions(
            name='messagerie',
            options={'verbose_name': 'Messagerie', 'verbose_name_plural': 'Messagerie'},
        ),
        migrations.AlterField(
            model_name='messagerie',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]