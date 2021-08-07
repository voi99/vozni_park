# Generated by Django 3.2.5 on 2021-08-01 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0007_vehicle_license_plate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurancepolicy',
            name='insurance_company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='company_polices', to='vehicle.insurancecompany'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='insurancepolicy',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='policy', to='vehicle.vehicle'),
        ),
    ]