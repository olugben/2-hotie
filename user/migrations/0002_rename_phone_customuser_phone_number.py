# Generated by Django 4.1.4 on 2023-01-04 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='phone',
            new_name='phone_number',
        ),
    ]
