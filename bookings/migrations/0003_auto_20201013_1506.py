# Generated by Django 3.0.3 on 2020-10-13 09:36

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_auto_20201013_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='seat',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3'), ('A4', 'A4'), ('A5', 'A5')], max_length=14),
        ),
    ]
