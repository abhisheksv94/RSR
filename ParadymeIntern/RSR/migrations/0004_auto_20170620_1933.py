# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-20 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RSR', '0003_auto_20170620_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='awards',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='person',
            name='certificate',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='person',
            name='conference',
            field=models.TextField(),
        ),
    ]