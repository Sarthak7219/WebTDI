# Generated by Django 4.2.4 on 2023-10-18 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_alter_household_arts_score_alter_household_ass_score_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tribe',
            name='image',
        ),
        migrations.AddField(
            model_name='tribe_image',
            name='tribe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tribe_image', to='home.tribe'),
        ),
    ]
