# Generated by Django 3.2.5 on 2021-07-29 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0005_auto_20210729_1449'),
        ('employee', '0004_rename_refueling_refuel'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='contact',
            field=models.CharField(default='068786041', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='refuel',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_refuels', to='employee.employee'),
        ),
        migrations.AlterField(
            model_name='refuel',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_refuels', to='vehicle.vehicle'),
        ),
        migrations.CreateModel(
            name='VehicleBreakdown',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=1000)),
                ('date', models.DateField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_vehicle_breakdowns', to='employee.employee')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_brekadowns', to='vehicle.vehicle')),
            ],
        ),
    ]
