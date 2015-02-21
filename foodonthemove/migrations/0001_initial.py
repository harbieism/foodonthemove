# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('email', models.EmailField(max_length=75, unique=True, null=True, blank=True)),
                ('username', models.CharField(unique=True, max_length=40)),
                ('phone_number', models.CharField(max_length=40, blank=True)),
                ('contact_text', models.BooleanField(default=False)),
                ('contact_call', models.BooleanField(default=False)),
                ('contact_email', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('is_admin', models.BooleanField(default=False)),
                ('address', models.CharField(max_length=40, blank=True)),
                ('zip_code', models.CharField(max_length=20, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
