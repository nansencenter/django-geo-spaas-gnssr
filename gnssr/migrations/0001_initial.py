# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 12:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GNSSR',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('catalog.dataset',),
        ),
    ]
