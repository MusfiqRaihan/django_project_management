# Generated by Django 3.1.5 on 2021-02-04 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_details', '0011_projectpaymentdone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectpaymentdone',
            name='budget',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projectpaymentdone',
            name='due',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projectpaymentdone',
            name='previous_payment',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
