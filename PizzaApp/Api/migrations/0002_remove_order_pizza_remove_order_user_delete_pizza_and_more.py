# Generated by Django 5.1.4 on 2024-12-28 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='pizza',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.DeleteModel(
            name='Pizza',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
