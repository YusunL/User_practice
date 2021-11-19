# Generated by Django 3.2.9 on 2021-11-19 10:04

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=190, unique=True)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', app.models.CustomUserManager()),
            ],
        ),
    ]
