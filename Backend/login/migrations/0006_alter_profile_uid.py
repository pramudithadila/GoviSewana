# Generated by Django 5.0.3 on 2024-03-12 08:39

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_profile_phone_number_alter_profile_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('0bc61935-d1f1-4a83-8610-035db3706de1')),
        ),
    ]
