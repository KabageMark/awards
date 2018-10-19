# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-19 12:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awardsapp', '0003_auto_20181019_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_description',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='design',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='usability',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], null=True),
        ),
    ]
