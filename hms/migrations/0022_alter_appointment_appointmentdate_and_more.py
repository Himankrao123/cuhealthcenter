# Generated by Django 4.0.4 on 2022-05-05 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0021_alter_appointment_appointmentdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointmentdate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='appointmenttime',
            field=models.TimeField(),
        ),
    ]
