# Generated by Django 4.2.4 on 2023-10-18 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_remove_tribe_image_tribe_image_tribe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tribe_image',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tribe_image',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
