# Generated by Django 4.2.3 on 2024-02-23 14:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("fitness", "0002_rename_puja_date_course_buy_therapy_date"),
    ]

    operations = [
        migrations.RenameField(
            model_name="course_buy",
            old_name="puja_name",
            new_name="course_name",
        ),
    ]
