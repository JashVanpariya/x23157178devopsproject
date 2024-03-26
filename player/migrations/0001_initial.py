# Generated by Django 2.1.15 on 2024-03-16 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=200)),
                ('player_email', models.EmailField(max_length=254)),
                ('player_contact', models.CharField(max_length=20)),
                ('player_role', models.CharField(max_length=200)),
                ('player_salary', models.IntegerField()),
            ],
        ),
    ]
