# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-06-26 05:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Families',
            new_name='Family',
        ),
        migrations.RenameModel(
            old_name='Individuals',
            new_name='Individual',
        ),
        migrations.RenameModel(
            old_name='Relationships',
            new_name='Relationship',
        ),
        migrations.RenameModel(
            old_name='Relationship_Types',
            new_name='Relationship_Type',
        ),
        migrations.RenameModel(
            old_name='Roles',
            new_name='Role',
        ),
    ]
