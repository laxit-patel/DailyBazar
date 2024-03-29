# Generated by Django 2.2.6 on 2019-10-12 08:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('vendor_id', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('vendor_name', models.CharField(max_length=64)),
                ('vendor_email', models.CharField(max_length=64)),
                ('vendor_password', models.CharField(max_length=64)),
                ('vendor_phone', models.CharField(max_length=16)),
                ('vendor_city', models.CharField(max_length=64)),
                ('vendor_state', models.CharField(max_length=64)),
                ('vendor_country', models.CharField(max_length=64)),
                ('vendor_longitude', models.CharField(max_length=128)),
                ('vendor_latitude', models.CharField(max_length=128)),
                ('vendor_joined', models.DateTimeField(default=datetime.datetime.now)),
                ('vendor_exist', models.BooleanField(default=True)),
            ],
        ),
    ]
