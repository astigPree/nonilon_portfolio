# Generated by Django 4.2.21 on 2025-05-24 11:15

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_code', models.CharField(default=base.models.generate_client_code, max_length=15)),
                ('name', models.CharField(default='Your Name', max_length=15)),
                ('testimony', models.TextField(default='Write your testimony here', max_length=335)),
                ('rating', models.SmallIntegerField(default=3)),
                ('is_used', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='HardwareProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('description', models.TextField()),
                ('link', models.TextField(default='#')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='OtherLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('rating', models.IntegerField(default=50)),
                ('icon', models.FileField(upload_to='images/', validators=[base.models.validate_svg])),
                ('link', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='ProgrammingLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('rating', models.IntegerField(default=50)),
                ('icon', models.FileField(upload_to='images/', validators=[base.models.validate_svg])),
                ('link', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='SoftwareProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('description', models.TextField()),
                ('link', models.TextField(default='#')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='UsedFrameWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('rating', models.IntegerField(default=50)),
                ('icon', models.FileField(upload_to='images/', validators=[base.models.validate_svg])),
                ('link', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='UsedLibrary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('rating', models.IntegerField(default=50)),
                ('icon', models.FileField(upload_to='images/', validators=[base.models.validate_svg])),
                ('link', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='UsedSoftware',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('rating', models.IntegerField(default=50)),
                ('icon', models.FileField(upload_to='images/', validators=[base.models.validate_svg])),
                ('link', models.TextField(default='')),
            ],
        ),
    ]
