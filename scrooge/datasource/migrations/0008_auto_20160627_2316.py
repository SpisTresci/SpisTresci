# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-27 21:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datasource', '0007_auto_20160627_2316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='xmldatafield',
            old_name='datafield_name',
            new_name='name',
        ),
        migrations.AlterUniqueTogether(
            name='xmldatafield',
            unique_together=set([('name', 'data_source')]),
        ),
    ]
