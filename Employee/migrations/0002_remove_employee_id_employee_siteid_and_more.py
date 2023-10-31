# Generated by Django 4.2.2 on 2023-08-16 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Department', '0002_remove_department_id_alter_department_departmentid'),
        ('Site', '0002_remove_site_id_alter_site_siteid'),
        ('Employee', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='id',
        ),
        migrations.AddField(
            model_name='employee',
            name='SiteID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Site.site'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='DepartmentID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Department.department'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='EmployeeID',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
