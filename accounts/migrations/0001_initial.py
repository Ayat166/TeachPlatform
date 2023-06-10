# Generated by Django 4.1.5 on 2023-06-09 15:09

import accounts.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_options', models.CharField(choices=[('Teacher', 'Teacher'), ('Student', 'Student')], default=None, max_length=7, null=True, verbose_name='user-options')),
                ('first_name', models.CharField(blank=True, max_length=20, null=True, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=20, null=True, verbose_name='last name')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to=accounts.models.upload_profile_image_media, verbose_name='profile mage')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'db_table': 'users',
            },
        ),
    ]
