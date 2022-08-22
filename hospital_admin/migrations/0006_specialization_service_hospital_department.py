# Generated by Django 4.1 on 2022-08-22 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0009_report_prescription'),
        ('hospital', '0006_patient_serial_number'),
        ('hospital_admin', '0005_clinical_laboratory_technician'),
    ]

    operations = [
        migrations.CreateModel(
            name='specialization',
            fields=[
                ('specialization_id', models.AutoField(primary_key=True, serialize=False)),
                ('specialization_name', models.CharField(blank=True, max_length=200, null=True)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor_information')),
                ('hospital', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.hospital_information')),
            ],
        ),
        migrations.CreateModel(
            name='service',
            fields=[
                ('service_id', models.AutoField(primary_key=True, serialize=False)),
                ('service_name', models.CharField(blank=True, max_length=200, null=True)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor_information')),
                ('hospital', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.hospital_information')),
            ],
        ),
        migrations.CreateModel(
            name='hospital_department',
            fields=[
                ('hospital_department_id', models.AutoField(primary_key=True, serialize=False)),
                ('hospital_department_name', models.CharField(blank=True, max_length=200, null=True)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor_information')),
                ('hospital', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.hospital_information')),
            ],
        ),
    ]
