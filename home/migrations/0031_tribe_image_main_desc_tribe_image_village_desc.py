# Generated by Django 4.2.4 on 2023-10-19 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_tribe_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='tribe_image',
            name='main_desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tribe_image',
            name='village_desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
