# Generated by Django 2.2.3 on 2019-08-19 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20190817_1336'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='parentid',
            new_name='parent_id',
        ),
    ]
