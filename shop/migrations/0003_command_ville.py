# Generated by Django 4.1.7 on 2023-10-04 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_command'),
    ]

    operations = [
        migrations.AddField(
            model_name='command',
            name='ville',
            field=models.CharField(default=False, max_length=300),
        ),
    ]