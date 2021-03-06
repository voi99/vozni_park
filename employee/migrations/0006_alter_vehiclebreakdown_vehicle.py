# Generated by Django 3.2.5 on 2021-08-01 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0007_vehicle_license_plate'),
        ('employee', '0005_auto_20210729_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiclebreakdown',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_breakdowns', to='vehicle.vehicle'),
        ),
    ]
