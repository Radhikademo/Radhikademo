# Generated by Django 3.2.14 on 2023-05-21 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=50)),
                ('Last_Name', models.CharField(max_length=50)),
                ('User_Name', models.EmailField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=100)),
                ('pwd', models.CharField(max_length=50)),
            ],
        ),
    ]
