# Generated by Django 5.0.4 on 2024-04-16 23:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DriveAxleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EngineModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MaintenanceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MashineModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RecoveryMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RefusalNode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SteeringAxleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TransmissionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mashine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factory_mashine_number', models.TextField(unique=True)),
                ('factory_engine_number', models.TextField()),
                ('factory_transmission_number', models.TextField()),
                ('factory_drive_axle_number', models.TextField()),
                ('factory_steering_axle_number', models.TextField()),
                ('supply_agreement', models.TextField(help_text='№, date', null=True)),
                ('factory_shipment_date', models.DateField()),
                ('consignee', models.TextField(help_text='end-user')),
                ('delivery_address', models.TextField()),
                ('equipment', models.TextField(help_text='extra options')),
                ('client', models.TextField()),
                ('drive_axle_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silantmashinesapp.driveaxlemodel')),
                ('engine_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silantmashinesapp.enginemodel')),
                ('mashine_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silantmashinesapp.mashinemodel')),
                ('service_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silantmashinesapp.servicecompany')),
                ('steering_axle_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silantmashinesapp.steeringaxlemodel')),
                ('transmission_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silantmashinesapp.transmissionmodel')),
            ],
        ),
        migrations.CreateModel(
            name='Maintence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintence_date', models.DateField()),
                ('operating_time', models.IntegerField(help_text='meters per hours')),
                ('work_order_number', models.TextField()),
                ('work_order_date', models.DateField()),
                ('maintence_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silantmashinesapp.maintenancetype')),
                ('mashine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silantmashinesapp.mashine')),
                ('service_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silantmashinesapp.servicecompany')),
            ],
        ),
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refusal_date', models.DateField()),
                ('operating_time', models.FloatField(help_text='meters per hours')),
                ('refusal_description', models.TextField()),
                ('spare_parts_used', models.TextField()),
                ('recovery_date', models.DateField()),
                ('mashine_downtime', models.TextField()),
                ('mashine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silantmashinesapp.mashine')),
                ('recovery_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silantmashinesapp.recoverymethod')),
                ('refusal_node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silantmashinesapp.refusalnode')),
                ('service_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silantmashinesapp.servicecompany')),
            ],
        ),
    ]