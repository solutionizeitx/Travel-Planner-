# Generated by Django 4.2.5 on 2023-12-24 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelApp', '0002_alter_hotel_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='banner_image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='normal_image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
