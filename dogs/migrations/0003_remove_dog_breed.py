# Generated by Django 4.2.5 on 2023-10-03 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0002_alter_dog_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dog',
            name='breed',
        ),
    ]
