# Generated by Django 4.2.5 on 2023-10-21 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(blank=True, null=True, unique=True)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('st_population', models.IntegerField()),
                ('total_population', models.IntegerField()),
                ('W_BMI', models.FloatField()),
                ('C_UW', models.FloatField()),
                ('AN_W', models.FloatField()),
                ('AN_C', models.FloatField()),
                ('AHC_ANC', models.FloatField()),
                ('AHC_Full_ANC', models.FloatField()),
                ('AHC_PNC', models.FloatField()),
                ('AHC_HI', models.FloatField()),
                ('Enrollment', models.FloatField()),
                ('Equity', models.FloatField()),
                ('E_DropRate', models.FloatField()),
                ('S_Sani', models.FloatField()),
                ('S_CoFu', models.FloatField()),
                ('S_DrWa', models.FloatField()),
                ('S_Elec', models.FloatField()),
            ],
        ),
    ]
