# Generated by Django 3.1.5 on 2021-02-04 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_details', '0009_auto_20210204_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeline_user',
            name='completion_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='timeline_user',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
