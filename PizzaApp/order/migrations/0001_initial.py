# Generated by Django 5.1.4 on 2024-12-28 06:21

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pizza', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('Picked-up', 'On Transit'), ('Delivered', 'Received')], default='Picked-up', max_length=30, null=True)),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='pizza.pizza')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
