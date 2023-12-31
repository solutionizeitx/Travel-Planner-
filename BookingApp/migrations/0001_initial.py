# Generated by Django 4.2.5 on 2023-09-17 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('PackageApp', '0002_alter_package_name_alter_packagetype_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_date', models.DateField(auto_now=True, null=True)),
                ('packageId', models.IntegerField(blank=True, null=True)),
                ('packageName', models.CharField(max_length=15)),
                ('hotel', models.CharField(max_length=25)),
                ('hotelId', models.IntegerField(blank=True, null=True)),
                ('hotel_name', models.CharField(max_length=25)),
                ('type', models.DecimalField(decimal_places=2, max_digits=20)),
                ('typeId', models.IntegerField(blank=True, null=True)),
                ('typeName', models.CharField(max_length=25)),
                ('package_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('hotel_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('booking_date_from', models.DateTimeField()),
                ('booking_date_to', models.DateTimeField()),
                ('discount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('number_of_people', models.IntegerField()),
                ('is_paid', models.BooleanField(default=False)),
                ('booking_status', models.BooleanField(default=False)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='PackageApp.package')),
            ],
        ),
    ]
