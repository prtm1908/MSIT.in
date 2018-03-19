# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-19 10:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0011_researchrecord_indexing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='researchrecord',
            name='year',
        ),
        migrations.AddField(
            model_name='researchrecord',
            name='issue',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Issue'),
        ),
        migrations.AddField(
            model_name='researchrecord',
            name='name_of_conference',
            field=models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='Name of Conference/Journal'),
        ),
        migrations.AddField(
            model_name='researchrecord',
            name='volume',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Volume'),
        ),
    ]