# Generated by Django 3.1.5 on 2021-02-08 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_details', '0018_remove_projectmonthlypayment_month_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='staff',
            new_name='user',
        ),
    ]
