# Generated by Django 4.2 on 2023-06-04 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dulc_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dulcinea',
            name='desc',
            field=models.TextField(max_length=500),
        ),
    ]