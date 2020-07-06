# Generated by Django 2.2 on 2020-07-03 17:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('toots', '0006_auto_20200701_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toot',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='toots', to=settings.AUTH_USER_MODEL),
        ),
    ]