# Generated by Django 2.2.14 on 2020-12-01 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0011_auto_20201201_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='income',
            field=models.CharField(choices=[('10,00,000', '10,00,000'), ('5,00,000', '5,00,000'), ('Below 5 Lakh', 'Below 5 Lakh')], default='', max_length=100),
        ),
    ]
