# Generated by Django 2.2 on 2020-08-12 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Web_App', '0009_class'),
    ]

    operations = [
        migrations.RenameField(
            model_name='class',
            old_name='book',
            new_name='sec',
        ),
    ]
