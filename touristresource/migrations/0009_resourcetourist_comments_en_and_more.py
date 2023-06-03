# Generated by Django 4.1.3 on 2023-05-29 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('touristresource', '0008_alter_resourcetourist_idmunicipality'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourcetourist',
            name='comments_en',
            field=models.TextField(blank=True, max_length=10000, null=True, verbose_name='Otros comentarios'),
        ),
        migrations.AddField(
            model_name='resourcetourist',
            name='comments_es',
            field=models.TextField(blank=True, max_length=10000, null=True, verbose_name='Otros comentarios'),
        ),
        migrations.AddField(
            model_name='resourcetourist',
            name='comments_fr',
            field=models.TextField(blank=True, max_length=10000, null=True, verbose_name='Otros comentarios'),
        ),
        migrations.AddField(
            model_name='resourcetourist',
            name='comments_ru',
            field=models.TextField(blank=True, max_length=10000, null=True, verbose_name='Otros comentarios'),
        ),
        migrations.AddField(
            model_name='resourcetourist',
            name='description_en',
            field=models.TextField(blank=True, max_length=10000, null=True, verbose_name='Descripción'),
        ),
        migrations.AddField(
            model_name='resourcetourist',
            name='description_es',
            field=models.TextField(blank=True, max_length=10000, null=True, verbose_name='Descripción'),
        ),
        migrations.AddField(
            model_name='resourcetourist',
            name='description_fr',
            field=models.TextField(blank=True, max_length=10000, null=True, verbose_name='Descripción'),
        ),
        migrations.AddField(
            model_name='resourcetourist',
            name='description_ru',
            field=models.TextField(blank=True, max_length=10000, null=True, verbose_name='Descripción'),
        ),
        migrations.AddField(
            model_name='resourcetourist',
            name='name_en',
            field=models.CharField(default='', max_length=30, null=True, verbose_name='Nombre'),
        ),
        migrations.AddField(
            model_name='resourcetourist',
            name='name_es',
            field=models.CharField(default='', max_length=30, null=True, verbose_name='Nombre'),
        ),
        migrations.AddField(
            model_name='resourcetourist',
            name='name_fr',
            field=models.CharField(default='', max_length=30, null=True, verbose_name='Nombre'),
        ),
        migrations.AddField(
            model_name='resourcetourist',
            name='name_ru',
            field=models.CharField(default='', max_length=30, null=True, verbose_name='Nombre'),
        ),
    ]