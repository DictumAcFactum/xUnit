# Generated by Django 3.0.8 on 2020-08-02 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drones', '0002_auto_20200802_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dronecategory',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
