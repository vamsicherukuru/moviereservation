# Generated by Django 3.0.3 on 2020-10-15 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0007_auto_20201013_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='basic_price',
            field=models.IntegerField(default=100),
        ),
    ]
