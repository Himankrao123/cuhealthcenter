# Generated by Django 4.0.4 on 2022-04-26 11:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0013_updates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updates',
            name='messageon',
            field=models.DateField(default=datetime.datetime(2022, 4, 26, 17, 21, 3, 728521)),
        ),
    ]
