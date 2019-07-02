# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-02 02:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('family', '0005_family_image_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='individual',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='individual',
            name='created_by',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='individual',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
