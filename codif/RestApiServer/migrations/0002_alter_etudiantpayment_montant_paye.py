# Generated by Django 3.2.7 on 2021-09-16 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestApiServer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiantpayment',
            name='montant_paye',
            field=models.IntegerField(choices=[('4000', '4000'), ('3000', '3000')], max_length=30),
        ),
    ]
