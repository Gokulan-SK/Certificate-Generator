# Generated by Django 4.2.1 on 2024-03-01 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0003_remove_completedgeneration_certificate_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='completedgeneration',
            old_name='certificate_data',
            new_name='certificate',
        ),
    ]
