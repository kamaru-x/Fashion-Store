# Generated by Django 4.0.6 on 2022-08-21 03:29

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
                ('Name', models.CharField(max_length=25)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=20)),
            ],
        ),
    ]