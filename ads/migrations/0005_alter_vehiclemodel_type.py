# Generated by Django 4.2.2 on 2023-11-14 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_alter_picture_filename_alter_picture_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiclemodel',
            name='type',
            field=models.CharField(choices=[('CTD', 'Citadine'), ('BLN', 'Berline'), ('SUV', 'SUV'), ('4x4', '4*4')], max_length=200, null=True),
        ),
    ]