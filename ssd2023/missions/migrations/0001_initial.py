# Generated by Django 4.2 on 2023-04-07 04:45

from django.db import migrations, models
import django.db.models.deletion
import missions.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=256)),
                ('lastName', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('_address', models.CharField(max_length=100)),
                ('_phoneNumber', models.CharField(max_length=14)),
                ('_socialSecurityNumber', missions.models.SecureCharField(max_length=104)),
                ('_securityClearance', models.SmallIntegerField()),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='missions.division')),
            ],
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('startDate', models.DateTimeField(verbose_name='Date of commencement')),
                ('endDate', models.DateTimeField(verbose_name='Date of completion')),
                ('_description', models.CharField(max_length=4096)),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='missions.division')),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='missions.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('location', models.CharField(max_length=100)),
                ('startDate', models.DateTimeField(verbose_name='Date of commencement')),
                ('endDate', models.DateTimeField(verbose_name='Date of completion')),
                ('_description', models.CharField(max_length=4096)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='missions.employee')),
                ('mission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='missions.mission')),
            ],
        ),
        migrations.CreateModel(
            name='Satellite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('location', models.CharField(max_length=100)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='missions.project')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024)),
                ('publishDate', models.DateTimeField(verbose_name='Date published')),
                ('_summary', models.CharField(max_length=4096)),
                ('assignedTo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='missions.employee')),
                ('mission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='missions.mission')),
            ],
        ),
    ]