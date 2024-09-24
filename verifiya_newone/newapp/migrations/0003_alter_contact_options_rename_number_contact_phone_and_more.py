# Generated by Django 5.0.6 on 2024-09-23 08:34

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_alter_contact_options_alter_contact_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={},
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='number',
            new_name='phone',
        ),
        migrations.AddField(
            model_name='internshipapplication',
            name='InternshipApplication_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
