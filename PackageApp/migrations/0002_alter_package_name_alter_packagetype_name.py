# Generated by Django 4.2.5 on 2023-09-16 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PackageApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='name',
            field=models.CharField(max_length=25, unique=True),
        ),
        migrations.AlterField(
            model_name='packagetype',
            name='name',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]