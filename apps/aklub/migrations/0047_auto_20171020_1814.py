# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-20 18:14
from __future__ import unicode_literals

import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aklub', '0046_auto_20171020_1510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='communication',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='communication',
            name='handled_by',
        ),
        migrations.RemoveField(
            model_name='userincampaign',
            name='verified_by',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='telephone',
            field=models.CharField(blank=True, max_length=100, validators=[django.core.validators.RegexValidator('^[0-9+ ]*$', 'Telephone must consist of numbers, spaces and + sign')], verbose_name='Telephone'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
        migrations.AlterModelOptions(
            name='userincampaign',
            options={'ordering': ['userprofile__last_name', 'userprofile__first_name'], 'verbose_name': 'User in campaign', 'verbose_name_plural': 'Users in campaign'},
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address', blank=True, null=True),
        ),
    ]