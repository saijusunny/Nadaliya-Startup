# Generated by Django 4.0.2 on 2023-07-21 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NadaliyaApp', '0002_remove_user_registration_email_otp_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_registration',
            name='status',
            field=models.CharField(blank=True, choices=[('Approved', 'Approved'), ('Declin', 'Declin')], max_length=255, null=True),
        ),
    ]
