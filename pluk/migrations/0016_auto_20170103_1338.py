# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-03 10:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pluk', '0015_auto_20161230_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='pluk.Article'),
        ),
    ]
