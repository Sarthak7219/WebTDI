# Generated by Django 4.2.4 on 2023-10-19 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_alter_tribe_image_main_desc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tribe_image',
            name='map_image',
            field=models.ImageField(default='e', upload_to='images'),
            preserve_default=False,
        ),
    ]
