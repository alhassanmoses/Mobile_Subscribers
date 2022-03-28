# Generated by Django 3.1.2 on 2022-03-28 02:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subscriber', '0002_auto_20220327_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobilesubscribermodel',
            name='customer_id_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Customer_id_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]