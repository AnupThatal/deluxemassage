# Generated by Django 4.2.3 on 2024-02-23 13:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("fitness", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="course_buy",
            old_name="puja_date",
            new_name="Therapy_date",
        ),
    ]