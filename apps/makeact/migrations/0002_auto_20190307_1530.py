# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-07 15:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('makeact', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activitys',
            name='brands',
        ),
        migrations.RemoveField(
            model_name='activitys',
            name='favo',
        ),
        migrations.RemoveField(
            model_name='activitys',
            name='signs',
        ),
        migrations.AlterField(
            model_name='activitys',
            name='image',
            field=models.ImageField(blank=True, help_text='单张图', null=True, upload_to='actimage/%Y/%m/%d/', verbose_name='单张图'),
        ),
        migrations.AlterField(
            model_name='activitys',
            name='user',
            field=models.ForeignKey(blank=True, help_text='用户id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='re_user', to=settings.AUTH_USER_MODEL, verbose_name='用户id'),
        ),
    ]
