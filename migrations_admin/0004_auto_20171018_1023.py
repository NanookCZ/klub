# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-18 10:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_auto_20171018_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logentry',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.User', verbose_name='user'),
        ),
    ]