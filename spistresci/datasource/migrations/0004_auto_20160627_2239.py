# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-27 20:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datasource', '0003_auto_20160627_1928'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='xmldatafield',
            unique_together=set([('name', 'data_source'), ('datafield_name', 'data_source')]),
        ),
    ]
