# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 01:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='dob',
            field=models.DateField(default='2000-12-21'),
        ),
    ]
