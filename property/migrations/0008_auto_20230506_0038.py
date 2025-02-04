# Generated by Django 2.2.24 on 2023-05-05 21:38

from django.db import migrations
import phonenumbers


def replace_with_pure_number(apps, schema_edition):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all().iterator():
        primary_phone_number = phonenumbers.parse(flat.owners_phonenumber, "RU")
        if phonenumbers.is_valid_number(primary_phone_number):
            flat.owner_pure_phone = phonenumbers.format_number(
                primary_phone_number, phonenumbers.PhoneNumberFormat.E164)
            flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(replace_with_pure_number)
    ]
