# Generated by Django 3.0.3 on 2020-10-13 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]
