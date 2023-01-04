# Generated by Django 4.1.3 on 2023-01-03 15:34

from django.db import migrations, models
import django.db.models.constraints
import django.db.models.deletion
import touristresource.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceTourist',
            fields=[
                ('idRT', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('name_es', models.CharField(max_length=100, null=True, verbose_name='Nombre')),
                ('name_en', models.CharField(max_length=100, null=True, verbose_name='Nombre')),
                ('description', models.TextField(max_length=100000, verbose_name='Descripción')),
                ('description_es', models.TextField(max_length=100000, null=True, verbose_name='Descripción')),
                ('description_en', models.TextField(max_length=100000, null=True, verbose_name='Descripción')),
                ('history', models.TextField(max_length=100000, verbose_name='Historia')),
                ('history_es', models.TextField(max_length=100000, null=True, verbose_name='Historia')),
                ('history_en', models.TextField(max_length=100000, null=True, verbose_name='Historia')),
                ('siteWeb', models.URLField(blank=True, max_length=50, null=True, verbose_name='Sitio Web')),
                ('slug', models.CharField(max_length=100, unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'Recurso turístico',
                'verbose_name_plural': 'Recursos turísticos',
            },
        ),
        migrations.CreateModel(
            name='ScheduleService',
            fields=[
                ('idScheduleClass', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('name_es', models.CharField(max_length=50, null=True, verbose_name='Nombre')),
                ('name_en', models.CharField(max_length=50, null=True, verbose_name='Nombre')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
                ('startTime', models.TimeField(verbose_name='Hora de inicio')),
                ('endTime', models.TimeField(verbose_name='Hora de terminacion')),
            ],
            options={
                'verbose_name': 'Horario de servicio',
                'verbose_name_plural': 'Horarios de servicio',
                'ordering': ('startTime', 'endTime', 'name'),
            },
        ),
        migrations.CreateModel(
            name='TourismType',
            fields=[
                ('idTT', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(default='', max_length=30, verbose_name='Tipo de turismo')),
                ('type_es', models.CharField(default='', max_length=30, null=True, verbose_name='Tipo de turismo')),
                ('type_en', models.CharField(default='', max_length=30, null=True, verbose_name='Tipo de turismo')),
                ('description', models.TextField(blank=True, max_length=10000, verbose_name='Descripción')),
                ('description_es', models.TextField(blank=True, max_length=10000, null=True, verbose_name='Descripción')),
                ('description_en', models.TextField(blank=True, max_length=10000, null=True, verbose_name='Descripción')),
                ('slug', models.CharField(max_length=30, unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'Tipo de turismo',
                'verbose_name_plural': 'Tipos de turismo',
                'ordering': ('type', 'description'),
            },
        ),
        migrations.CreateModel(
            name='TouristResourceVideo',
            fields=[
                ('idTRV', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Video del recurso turístico',
                'verbose_name_plural': 'Videos del recurso turístico',
            },
        ),
        migrations.CreateModel(
            name='TypeService',
            fields=[
                ('idTS', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(default='', max_length=30, verbose_name='Tipo de servicio')),
                ('type_es', models.CharField(default='', max_length=30, null=True, verbose_name='Tipo de servicio')),
                ('type_en', models.CharField(default='', max_length=30, null=True, verbose_name='Tipo de servicio')),
                ('description', models.TextField(blank=True, max_length=10000, verbose_name='Descripción')),
                ('description_es', models.TextField(blank=True, max_length=10000, null=True, verbose_name='Descripción')),
                ('description_en', models.TextField(blank=True, max_length=10000, null=True, verbose_name='Descripción')),
                ('slug', models.CharField(max_length=30, unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'Tipo de servicio',
                'verbose_name_plural': 'Tipos de servicios',
                'ordering': ('type', 'description'),
            },
        ),
        migrations.CreateModel(
            name='ValueTouristic',
            fields=[
                ('idVT', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(default='', max_length=40, verbose_name='Valor')),
                ('value_es', models.CharField(default='', max_length=40, null=True, verbose_name='Valor')),
                ('value_en', models.CharField(default='', max_length=40, null=True, verbose_name='Valor')),
                ('description', models.TextField(blank=True, max_length=10000, verbose_name='Descripción')),
                ('description_es', models.TextField(blank=True, max_length=10000, null=True, verbose_name='Descripción')),
                ('description_en', models.TextField(blank=True, max_length=10000, null=True, verbose_name='Descripción')),
                ('slug', models.SlugField(max_length=40, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'Valor turístico',
                'verbose_name_plural': 'Valores turísticos',
                'ordering': ('value', 'description'),
            },
        ),
        migrations.CreateModel(
            name='ValueResourceTourist',
            fields=[
                ('idVRT', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('idResourceTourist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='touristresource.resourcetourist', verbose_name='Recurso turístico')),
                ('idValueTouristic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='touristresource.valuetouristic', verbose_name='Valor turístico del recurso')),
            ],
            options={
                'verbose_name': 'Valor del recurso turístico',
                'verbose_name_plural': 'Valores del recurso turístico',
                'ordering': ('idResourceTourist', 'idValueTouristic'),
            },
        ),
        migrations.CreateModel(
            name='TouristResourceImage',
            fields=[
                ('idTRI', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre')),
                ('name_es', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre')),
                ('name_en', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre')),
                ('description', models.TextField(blank=True, max_length=255, null=True, verbose_name='Descripción')),
                ('description_es', models.TextField(blank=True, max_length=255, null=True, verbose_name='Descripción')),
                ('description_en', models.TextField(blank=True, max_length=255, null=True, verbose_name='Descripción')),
                ('image', models.ImageField(upload_to=touristresource.models.renameFile, verbose_name='Imagen del recurso')),
                ('slug', models.CharField(max_length=100, unique=True, verbose_name='slug')),
                ('idTouristResource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='touristresource.resourcetourist', verbose_name='Recurso Turísticos')),
            ],
            options={
                'verbose_name': 'Imagen del recurso turístico',
                'verbose_name_plural': 'Imágenes del recurso turístico',
            },
        ),
        migrations.CreateModel(
            name='TourismTypeResourceTourist',
            fields=[
                ('idTTRT', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('idResourceTourist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='touristresource.resourcetourist', verbose_name='Recurso turístico')),
                ('idTourismType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='touristresource.tourismtype', verbose_name='Tipo de turismo')),
            ],
            options={
                'verbose_name': 'Tipo de turismo del recurso turístico',
                'verbose_name_plural': 'Tipos de turismo del recurso turístico',
                'ordering': ('idResourceTourist', 'idTourismType'),
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('idService', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('idResourceTourist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='touristresource.resourcetourist', verbose_name='Recurso turístico')),
                ('idScheduleService', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='touristresource.scheduleservice', verbose_name='Horario del servicio')),
                ('idTypeService', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='touristresource.typeservice', verbose_name='Tipo de servicio')),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
                'ordering': ('idResourceTourist', 'idTypeService', 'idScheduleService'),
            },
        ),
        migrations.AddConstraint(
            model_name='scheduleservice',
            constraint=models.UniqueConstraint(deferrable=django.db.models.constraints.Deferrable['DEFERRED'], fields=('startTime', 'endTime'), name='unique_range_time'),
        ),
        migrations.AddConstraint(
            model_name='valueresourcetourist',
            constraint=models.UniqueConstraint(deferrable=django.db.models.constraints.Deferrable['DEFERRED'], fields=('idResourceTourist', 'idValueTouristic'), name='unique_value_tourist'),
        ),
        migrations.AddConstraint(
            model_name='tourismtyperesourcetourist',
            constraint=models.UniqueConstraint(deferrable=django.db.models.constraints.Deferrable['DEFERRED'], fields=('idResourceTourist', 'idTourismType'), name='unique_type_tourist'),
        ),
        migrations.AddConstraint(
            model_name='service',
            constraint=models.UniqueConstraint(deferrable=django.db.models.constraints.Deferrable['DEFERRED'], fields=('idResourceTourist', 'idTypeService', 'idScheduleService'), name='unique_service'),
        ),
    ]
