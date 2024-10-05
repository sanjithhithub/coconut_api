# Generated by Django 5.0.2 on 2024-10-05 10:08

import django.utils.timezone
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccapi', '0002_customerdetail_alter_employee_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerPurchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('coconut_count', models.PositiveIntegerField()),
                ('rate', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=5)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
