# Generated by Django 5.0.3 on 2024-03-12 07:05

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_alter_profile_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('9fb119ca-b837-4fe1-9289-3dd15341fa2c')),
        ),
    ]
