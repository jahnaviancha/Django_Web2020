# Generated by Django 2.2 on 2020-08-08 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Web_App', '0002_employee_username'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employee',
            new_name='Student',
        ),
        migrations.AlterModelTable(
            name='student',
            table='student',
        ),
    ]
