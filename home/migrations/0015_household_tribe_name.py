# Generated by Django 4.2.4 on 2023-09-04 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_remove_household_tribe_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='household',
            name='tribe_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
