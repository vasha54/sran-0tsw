# Generated by Django 4.0 on 2022-11-28 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('touristresource', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='touristresource',
            name='description',
            field=models.TextField(max_length=255, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='touristresourceimage',
            name='description',
            field=models.TextField(max_length=255, verbose_name='Descripción'),
        ),
    ]
