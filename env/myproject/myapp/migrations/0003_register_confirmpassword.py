# Generated by Django 5.0.1 on 2024-01-04 15:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0002_register"),
    ]

    operations = [
        migrations.AddField(
            model_name="register",
            name="confirmpassword",
            field=models.CharField(default=True, max_length=200),
        ),
    ]
