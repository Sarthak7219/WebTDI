# Generated by Django 4.2.4 on 2023-09-03 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_health_cd_score_alter_health_cm_score_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='household',
            name='size',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
