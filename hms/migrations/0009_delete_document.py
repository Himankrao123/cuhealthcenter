# Generated by Django 4.0.4 on 2022-04-20 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0008_remove_document_user_document_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Document',
        ),
    ]
