# Generated by Django 3.2.4 on 2021-11-26 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ValidationManagement', '0008_fieldvalidationmapping_new_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fieldvalidationmapping',
            name='new_field',
        ),
        migrations.DeleteModel(
            name='PayloadFieldMapping',
        ),
    ]
