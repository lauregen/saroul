# Generated by Django 4.2.2 on 2023-11-20 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0009_alter_picture_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
