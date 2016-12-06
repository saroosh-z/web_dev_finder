# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-06 01:06
from __future__ import unicode_literals

import address.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        ('authentication', '0010_userprofile_soundcloud_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='location',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=address.models.AddressField(null=True, on_delete=django.db.models.deletion.CASCADE, to='address.Address'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='address_lat',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='address_long',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
    ]
