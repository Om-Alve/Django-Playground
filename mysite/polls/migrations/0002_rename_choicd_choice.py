# Generated by Django 4.2.5 on 2023-09-06 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Choicd',
            new_name='Choice',
        ),
    ]
