# Generated by Django 4.2.1 on 2024-03-01 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_completedgeneration_certificate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='completedgeneration',
            name='certificate',
        ),
        migrations.AddField(
            model_name='completedgeneration',
            name='certificate_data',
            field=models.BinaryField(null=True),
        ),
    ]