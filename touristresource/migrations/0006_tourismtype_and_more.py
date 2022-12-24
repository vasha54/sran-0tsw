# Generated by Django 4.1.3 on 2022-12-23 12:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('touristresource', '0005_alter_touristresource_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='TourismType',
            fields=[
                ('idTT', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, verbose_name='Nombre')),
                ('description', models.TextField(max_length=10000, verbose_name='Descripción')),
            ],
        ),
        migrations.RemoveField(
            model_name='touristresourceimage',
            name='idTouristResource',
        ),
        migrations.DeleteModel(
            name='TouristResource',
        ),
        migrations.DeleteModel(
            name='TouristResourceImage',
        ),
    ]
