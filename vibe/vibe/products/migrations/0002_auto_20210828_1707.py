# Generated by Django 3.2.6 on 2021-08-28 10:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='descrition',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 28, 17, 7, 30, 387983)),
        ),
    ]
