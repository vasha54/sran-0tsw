# Generated by Django 4.1.3 on 2023-06-05 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('touristresource', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcetourist',
            name='geoLocLat',
            field=models.DecimalField(decimal_places=21, default=0.0, max_digits=25, verbose_name='Latitud'),
        ),
        migrations.AlterField(
            model_name='resourcetourist',
            name='geoLocLon',
            field=models.DecimalField(decimal_places=21, default=0.0, max_digits=25, verbose_name='Longitud'),
        ),
    ]
