# Generated by Django 4.2.2 on 2023-08-16 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Department', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='id',
        ),
        migrations.AlterField(
            model_name='department',
            name='DepartmentID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
