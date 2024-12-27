# Generated by Django 5.0.9 on 2024-12-04 12:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Admin', '0002_clipr_remove_superuser_unique_url_superuser_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProviderURL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=255)),
                ('project_name', models.CharField(max_length=255)),
                ('provider_id', models.IntegerField()),
                ('provider_name', models.CharField(max_length=255)),
                ('provider_email', models.EmailField(max_length=254)),
                ('provi_url', models.URLField()),
                ('cp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Admin.clientproject')),
            ],
        ),
        migrations.CreateModel(
            name='SuperUserURL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=255)),
                ('project_name', models.CharField(max_length=255)),
                ('superuser_name', models.CharField(max_length=255)),
                ('superuser_email', models.EmailField(max_length=254)),
                ('super_url', models.URLField()),
                ('cp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Admin.clientproject')),
            ],
        ),
    ]
