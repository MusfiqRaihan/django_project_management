# Generated by Django 3.1.5 on 2021-02-03 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_details', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectfeaturepayment',
            name='feature',
            field=models.JSONField(default=None),
        ),
    ]