# Generated by Django 4.1.7 on 2023-10-03 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=200)),
                ('pays', models.CharField(max_length=300)),
                ('zipcode', models.CharField(max_length=300)),
                ('command_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['command_date'],
            },
        ),
    ]
