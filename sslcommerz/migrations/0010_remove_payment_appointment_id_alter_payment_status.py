# Generated by Django 4.0.6 on 2022-08-14 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sslcommerz', '0009_remove_payment_appointment_payment_appointment_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='appointment_id',
        ),
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]