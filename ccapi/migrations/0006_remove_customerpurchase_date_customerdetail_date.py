# Generated by Django 5.0.2 on 2024-10-07 09:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccapi', '0005_customerpurchase_date_alter_customerpurchase_amount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerpurchase',
            name='date',
        ),
        migrations.AddField(
            model_name='customerdetail',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
