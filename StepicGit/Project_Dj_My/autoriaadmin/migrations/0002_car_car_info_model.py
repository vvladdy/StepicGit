# Generated by Django 4.1.2 on 2022-10-30 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoriaadmin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_info_model',
            field=models.ManyToManyField(related_name='models', to='autoriaadmin.carmodel'),
        ),
    ]
