# Generated by Django 4.2.5 on 2023-09-27 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_remove_tribe_ide'),
    ]

    operations = [
        migrations.AddField(
            model_name='household',
            name='decimal_field',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
