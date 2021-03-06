# Generated by Django 3.1.5 on 2021-02-06 10:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project_details', '0016_remove_projectpaymentdone_new_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectMonthlyPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_name', models.CharField(max_length=100)),
                ('monthly', models.JSONField(default=None)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('profile_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_details.projectdetail')),
            ],
        ),
    ]
