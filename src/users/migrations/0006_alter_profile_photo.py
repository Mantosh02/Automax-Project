# Generated by Django 5.1.1 on 2024-10-30 17:30

import users.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_location_alter_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=users.utils.user_directory_path),
        ),
    ]
