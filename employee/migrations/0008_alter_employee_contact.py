# Generated by Django 3.2.5 on 2021-08-08 11:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0007_accident_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='contact',
            field=models.IntegerField(validators=[django.core.validators.RegexValidator(regex='^[0-9]{9,10}$')]),
        ),
    ]
