# Generated by Django 5.0.1 on 2024-01-04 15:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0003_register_confirmpassword"),
    ]

    operations = [
        migrations.RenameField(
            model_name="register",
            old_name="address",
            new_name="mail",
        ),
        migrations.RemoveField(
            model_name="register",
            name="district",
        ),
    ]
