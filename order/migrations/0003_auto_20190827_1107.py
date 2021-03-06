# Generated by Django 2.2.3 on 2019-08-27 08:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20190823_1547'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='sname',
            new_name='city',
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='surname',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='note',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[('New', 'New'), ('Accepted', 'Accepted'), ('Preaparing', 'Preaparing'), ('OnShipping', 'OnShipping'), ('Completed', 'Completed')], default='New'),
        ),
    ]
