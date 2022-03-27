# Generated by Django 3.1.2 on 2022-03-27 16:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MobileSubscriberModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msisdn', models.CharField(max_length=16, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')])),
                ('service_type', models.CharField(choices=[('MOBILE_PREPAID', 'MOBILE_PREPAID'), ('MOBILE_POSTPAID', 'MOBILE_POSTPAID')], default=0, max_length=50)),
                ('service_start_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
