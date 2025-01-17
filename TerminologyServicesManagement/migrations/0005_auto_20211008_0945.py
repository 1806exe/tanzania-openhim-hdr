# Generated by Django 3.2.4 on 2021-10-08 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TerminologyServicesManagement', '0004_auto_20210929_1551'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cptcode',
            old_name='cpt_code',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='cptcode',
            old_name='cpt_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='icd10code',
            old_name='icd10_code',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='icd10code',
            old_name='icd10_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='icd10code',
            old_name='icd10_code_sub_category',
            new_name='sub_category',
        ),
        migrations.RenameField(
            model_name='icd10codesubcategory',
            old_name='icd10_code_category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='icd10subcode',
            old_name='icd10_code',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='icd10subcode',
            old_name='icd10_sub_code',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='icd10subcode',
            old_name='icd10_sub_code_description',
            new_name='sub_code',
        ),
        migrations.RemoveField(
            model_name='cptcode',
            name='cpt_code_sub_category',
        ),
        migrations.RemoveField(
            model_name='cptcodesubcategory',
            name='cpt_code_category',
        ),
        migrations.AddField(
            model_name='cptcode',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='code', to='TerminologyServicesManagement.cptcodesubcategory'),
        ),
        migrations.AddField(
            model_name='cptcodesubcategory',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='sub_category', to='TerminologyServicesManagement.cptcodecategory'),
        ),
    ]
