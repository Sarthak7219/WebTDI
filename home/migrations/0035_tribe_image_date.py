# Generated by Django 4.2.4 on 2023-10-19 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0034_tribe_image_map_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='tribe_image',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
