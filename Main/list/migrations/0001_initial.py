# Generated by Django 4.2.1 on 2024-03-01 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompletedGeneration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('generation_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]