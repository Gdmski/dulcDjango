# Generated by Django 4.2 on 2023-06-12 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dulc_app', '0006_alter_dulcinea_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='dulcinea',
            name='event_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
