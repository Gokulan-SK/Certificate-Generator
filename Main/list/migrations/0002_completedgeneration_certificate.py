# Generated by Django 4.2.1 on 2024-03-01 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='completedgeneration',
            name='certificate',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]