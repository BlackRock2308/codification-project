# Generated by Django 3.2.7 on 2021-09-18 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RestApiServer', '0010_alter_chambre_etage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codification',
            name='etudiant',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='etudiant_codifie', to='RestApiServer.etudiant'),
        ),
    ]
