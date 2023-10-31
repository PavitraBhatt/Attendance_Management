# Generated by Django 4.2.4 on 2023-08-09 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SiteID', models.CharField(max_length=100)),
                ('HouseNumber', models.CharField(max_length=100)),
                ('ApartmentNumber', models.CharField(max_length=100)),
                ('Landmark', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=100)),
                ('State', models.CharField(max_length=100)),
                ('PIN', models.IntegerField()),
                ('Latitude', models.FloatField()),
                ('Longtitude', models.FloatField()),
            ],
        ),
    ]