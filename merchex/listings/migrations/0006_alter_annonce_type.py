# Generated by Django 4.1 on 2022-08-27 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_annonce_band'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annonce',
            name='type',
            field=models.CharField(choices=[('R', 'Records'), ('C', 'Clothing'), ('P', 'Posters'), ('M', 'Misc')], max_length=20),
        ),
    ]
