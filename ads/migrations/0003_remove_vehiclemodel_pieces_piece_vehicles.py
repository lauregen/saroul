# Generated by Django 4.2.2 on 2023-11-12 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_alter_vehiclemodel_pieces_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiclemodel',
            name='pieces',
        ),
        migrations.AddField(
            model_name='piece',
            name='vehicles',
            field=models.ManyToManyField(blank=True, null=True, through='ads.Ad', to='ads.vehiclemodel'),
        ),
    ]
