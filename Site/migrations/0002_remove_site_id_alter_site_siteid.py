# Generated by Django 4.2.2 on 2023-08-16 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='site',
            name='id',
        ),
        migrations.AlterField(
            model_name='site',
            name='SiteID',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]