# Generated by Django 3.2.4 on 2021-10-15 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deathbydiseasecaseatfacilityitems',
            name='first_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deathbydiseasecaseatfacilityitems',
            name='last_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deathbydiseasecaseatfacilityitems',
            name='middle_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
