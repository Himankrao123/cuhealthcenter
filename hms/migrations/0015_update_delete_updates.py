# Generated by Django 4.0.4 on 2022-04-26 11:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0014_alter_updates_messageon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('messageis', models.CharField(max_length=1000)),
                ('messageby', models.CharField(max_length=100)),
                ('messageon', models.DateField(default=datetime.datetime(2022, 4, 26, 17, 22, 22, 518007))),
            ],
        ),
        migrations.DeleteModel(
            name='Updates',
        ),
    ]
