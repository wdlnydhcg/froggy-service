# Generated by Django 2.1.5 on 2019-01-18 06:25

import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cases', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(storage=django.core.files.storage.FileSystemStorage(base_url='/media/casefile/', location='/app/media/casefile'), upload_to='', verbose_name='Case File')),
                ('file_name', models.CharField(blank=True, editable=False, max_length=255, null=True, verbose_name='File Name')),
                ('upload_time', models.DateTimeField(auto_now=True, verbose_name='Upload Time')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='casefiles', to='cases.Case', verbose_name='Case File')),
            ],
        ),
        migrations.CreateModel(
            name='TempFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_uuid', models.UUIDField(default=uuid.uuid4, verbose_name='UUID')),
                ('file', models.FileField(storage=django.core.files.storage.FileSystemStorage(base_url='/media/tempfile/', location='/app/media/tempfile'), upload_to='', verbose_name='Temp file')),
                ('file_name', models.CharField(blank=True, editable=False, max_length=255, null=True, verbose_name='File Name')),
                ('size', models.PositiveIntegerField(editable=False, verbose_name='Size')),
                ('upload_time', models.DateTimeField(auto_now=True, verbose_name='Upload Time')),
            ],
        ),
    ]
