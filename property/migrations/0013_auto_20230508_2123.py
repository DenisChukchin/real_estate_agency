# Generated by Django 2.2.24 on 2023-05-08 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20230507_2340'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='owner',
            new_name='name',
        ),
    ]
