# Generated by Django 4.2.4 on 2023-09-03 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_household_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='household',
            name='CD_score',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='household',
            name='CM_score',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='household',
            name='FS_score',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='household',
            name='IM_score',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='household',
            name='MC_score',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='household',
            name='no_of_H_indicators',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]