# Generated by Django 4.1.10 on 2023-09-03 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=200)),
                ('Lastname', models.CharField(max_length=200)),
                ('Email', models.CharField(max_length=200, unique=True)),
                ('Password', models.CharField(max_length=200)),
            ],
        ),
    ]
