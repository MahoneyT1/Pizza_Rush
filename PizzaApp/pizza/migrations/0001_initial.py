# Generated by Django 5.1.4 on 2025-01-02 16:53

import pizza.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.UUIDField(blank=True, default=pizza.models.generate_uuid, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description_type', models.CharField(max_length=200)),
                ('ingredients', models.CharField(max_length=200)),
                ('price', models.FloatField(default=0, max_length=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='pizza/images/')),
            ],
        ),
    ]
