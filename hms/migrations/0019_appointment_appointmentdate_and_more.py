# Generated by Django 4.0.4 on 2022-05-05 10:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0018_doctor_docdesc_alter_updatenew_messageon'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='appointmentdate',
            field=models.DateField(default=datetime.datetime(2022, 5, 5, 15, 57, 6, 699293)),
        ),
        migrations.AddField(
            model_name='appointment',
            name='appointmenttime',
            field=models.TimeField(default=datetime.datetime(2022, 5, 5, 15, 57, 6, 699292)),
        ),
        migrations.AlterField(
            model_name='updatenew',
            name='messageon',
            field=models.DateField(default=datetime.datetime(2022, 5, 5, 15, 57, 6, 699293)),
        ),
    ]
