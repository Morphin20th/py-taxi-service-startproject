# Generated by Django 5.1.1 on 2024-09-15 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("taxi", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="driver",
            options={"verbose_name": "Driver", "verbose_name_plural": "Drivers"},
        ),
        migrations.RenameField(
            model_name="driver",
            old_name="licence_number",
            new_name="license_number",
        ),
    ]