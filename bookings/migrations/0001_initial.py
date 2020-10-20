# Generated by Django 3.0.3 on 2020-10-13 05:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('poster', models.ImageField(blank=True, upload_to='movie_posters')),
                ('thumbnail', models.ImageField(null=True, upload_to='thumbnails')),
                ('director', models.CharField(default='', max_length=100)),
                ('starring', models.CharField(default='', max_length=100)),
                ('genres', models.CharField(default='', max_length=100)),
                ('description', models.CharField(default='', max_length=1000)),
                ('trailer', models.FileField(null=True, upload_to='trailer_videos')),
                ('language', models.CharField(choices=[('Telugu', 'Telugu'), ('Hindi', 'Hindi'), ('Malayalam', 'Malayalam'), ('Tamil', 'Tamil'), ('English', 'English')], default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bio', models.CharField(default='', max_length=100)),
                ('profilePic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='anonymous', max_length=100)),
                ('seat', models.CharField(choices=[('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3'), ('A4', 'A4'), ('A5', 'A5')], max_length=100)),
                ('show_timing', models.CharField(choices=[('8:30 AM', '8:30 AM'), ('11:30 AM', '11:30 AM'), ('2:30 PM', '2:30 PM'), ('6:30 PM', '6:30 PM'), ('9:30 PM', '9:30 PM')], default='6:30 PM', max_length=100)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.Movie')),
            ],
            options={
                'unique_together': {('movie', 'seat', 'show_timing')},
            },
        ),
    ]