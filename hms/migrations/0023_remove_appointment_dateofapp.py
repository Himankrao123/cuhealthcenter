# Generated by Django 4.0.4 on 2022-05-05 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0022_alter_appointment_appointmentdate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='dateofapp',
        ),
    ]