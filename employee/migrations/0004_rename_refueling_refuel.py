# Generated by Django 3.2.5 on 2021-07-28 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0004_auto_20210727_2053'),
        ('employee', '0003_refueling'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Refueling',
            new_name='Refuel',
        ),
    ]
