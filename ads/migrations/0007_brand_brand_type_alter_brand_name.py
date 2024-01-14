# Generated by Django 4.2.2 on 2023-11-20 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0006_alter_vehiclemodel_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='brand_type',
            field=models.CharField(choices=[('V', 'vehicle'), ('P', 'Piece')], default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
    ]
