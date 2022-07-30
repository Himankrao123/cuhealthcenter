# Generated by Django 3.2.12 on 2022-04-01 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('emailid', models.EmailField(max_length=254)),
                ('contactnumber', models.IntegerField()),
                ('subjecttocontact', models.TextField()),
                ('desc', models.TextField()),
                ('dateofcontact', models.DateTimeField()),
            ],
        ),
    ]
