# Generated by Django 4.2.5 on 2023-09-27 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_household_decimal_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='household',
            name='decimal_field',
        ),
    ]