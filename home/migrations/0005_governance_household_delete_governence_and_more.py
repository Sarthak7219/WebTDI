# Generated by Django 4.2.4 on 2023-09-03 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20230903_0940'),
    ]

    operations = [
        migrations.CreateModel(
            name='Governance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_indicators', models.IntegerField(blank=True, null=True)),
                ('EV_score', models.BooleanField(blank=True, null=True)),
                ('MEET_score', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Household',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HH_size', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Governence',
        ),
        migrations.RenameField(
            model_name='culture',
            old_name='HH_Score_C_Arts',
            new_name='ARTS_score',
        ),
        migrations.RenameField(
            model_name='culture',
            old_name='HH_Score_C_L',
            new_name='LAN_score',
        ),
        migrations.RenameField(
            model_name='culture',
            old_name='HH_size',
            new_name='no_of_indicators',
        ),
        migrations.RenameField(
            model_name='education',
            old_name='HH_Score_E_DRO',
            new_name='DRO_score',
        ),
        migrations.RenameField(
            model_name='education',
            old_name='HH_Score_E_LE',
            new_name='LE_score',
        ),
        migrations.RenameField(
            model_name='education',
            old_name='E_H_members_of_developed_HHs',
            new_name='no_of_indicators',
        ),
        migrations.RenameField(
            model_name='health',
            old_name='HH_Score_H_CD',
            new_name='CD_score',
        ),
        migrations.RenameField(
            model_name='health',
            old_name='HH_Score_H_FS',
            new_name='CM_score',
        ),
        migrations.RenameField(
            model_name='health',
            old_name='HH_Score_H_IMM',
            new_name='FS_score',
        ),
        migrations.RenameField(
            model_name='health',
            old_name='HH_Score_H_MC',
            new_name='IM_score',
        ),
        migrations.RenameField(
            model_name='health',
            old_name='HH_Score_H_U5C',
            new_name='MC_score',
        ),
        migrations.RenameField(
            model_name='health',
            old_name='HH_size',
            new_name='no_of_indicators',
        ),
        migrations.RenameField(
            model_name='sol',
            old_name='HH_Score_S_ASS',
            new_name='ASS_score',
        ),
        migrations.RenameField(
            model_name='sol',
            old_name='HH_Score_S_ELECTR',
            new_name='DRWA_score',
        ),
        migrations.RenameField(
            model_name='sol',
            old_name='HH_Score_S_Fuel',
            new_name='ELECTR_score',
        ),
        migrations.RenameField(
            model_name='sol',
            old_name='HH_Score_S_IC',
            new_name='FUEL_score',
        ),
        migrations.RenameField(
            model_name='sol',
            old_name='HH_Score_S_OWN',
            new_name='IC_score',
        ),
        migrations.RenameField(
            model_name='sol',
            old_name='HH_Score_S_SANI',
            new_name='OW_score',
        ),
        migrations.RenameField(
            model_name='sol',
            old_name='HH_Score_S_SoDrWa',
            new_name='SANI_score',
        ),
        migrations.RenameField(
            model_name='sol',
            old_name='HH_size',
            new_name='no_of_indicators',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='C_H_members_of_developed_HHs',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='C_incidence',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='C_intensity',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='Is_Developed',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='Weightage',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='developed_indicator',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='score',
        ),
        migrations.RemoveField(
            model_name='culture',
            name='total_indicator',
        ),
        migrations.RemoveField(
            model_name='education',
            name='E_incidence',
        ),
        migrations.RemoveField(
            model_name='education',
            name='E_intensity',
        ),
        migrations.RemoveField(
            model_name='education',
            name='HH_size',
        ),
        migrations.RemoveField(
            model_name='education',
            name='Is_Developed',
        ),
        migrations.RemoveField(
            model_name='education',
            name='Weightage',
        ),
        migrations.RemoveField(
            model_name='education',
            name='developed_indicator',
        ),
        migrations.RemoveField(
            model_name='education',
            name='score',
        ),
        migrations.RemoveField(
            model_name='education',
            name='total_indicator',
        ),
        migrations.RemoveField(
            model_name='health',
            name='H_H_members_of_developed_HHs',
        ),
        migrations.RemoveField(
            model_name='health',
            name='H_incidence',
        ),
        migrations.RemoveField(
            model_name='health',
            name='H_intensity',
        ),
        migrations.RemoveField(
            model_name='health',
            name='Is_Developed',
        ),
        migrations.RemoveField(
            model_name='health',
            name='Weightage',
        ),
        migrations.RemoveField(
            model_name='health',
            name='developed_indicator',
        ),
        migrations.RemoveField(
            model_name='health',
            name='score',
        ),
        migrations.RemoveField(
            model_name='health',
            name='total_indicator',
        ),
        migrations.RemoveField(
            model_name='sol',
            name='Is_Developed',
        ),
        migrations.RemoveField(
            model_name='sol',
            name='S_H_members_of_developed_HHs',
        ),
        migrations.RemoveField(
            model_name='sol',
            name='S_incidence',
        ),
        migrations.RemoveField(
            model_name='sol',
            name='S_intensity',
        ),
        migrations.RemoveField(
            model_name='sol',
            name='Weightage',
        ),
        migrations.RemoveField(
            model_name='sol',
            name='developed_indicator',
        ),
        migrations.RemoveField(
            model_name='sol',
            name='score',
        ),
        migrations.RemoveField(
            model_name='sol',
            name='total_indicator',
        ),
        migrations.AddField(
            model_name='tribe',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tribe_image', to='home.tribe_image'),
        ),
        migrations.AddField(
            model_name='household',
            name='tribe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='household', to='home.tribe'),
        ),
        migrations.AddField(
            model_name='governance',
            name='HH',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='governance', to='home.household'),
        ),
        migrations.AddField(
            model_name='culture',
            name='HH',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='culture', to='home.household'),
        ),
        migrations.AddField(
            model_name='education',
            name='HH',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='education', to='home.household'),
        ),
        migrations.AddField(
            model_name='health',
            name='HH',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='health', to='home.household'),
        ),
        migrations.AddField(
            model_name='sol',
            name='HH',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sol', to='home.household'),
        ),
    ]
