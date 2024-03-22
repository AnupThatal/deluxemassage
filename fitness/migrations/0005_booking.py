# Generated by Django 5.0.1 on 2024-03-21 10:25

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fitness", "0004_rename_course_name_course_buy_therpay_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Booking",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("user_name", models.CharField(max_length=150)),
                ("user_email", models.EmailField(max_length=150)),
                ("user_contact", models.CharField(max_length=20)),
                ("booking_date", models.DateField(default=datetime.datetime.now)),
                ("message", models.TextField(blank=True, null=True)),
                ("status", models.CharField(default="Pending", max_length=50)),
                (
                    "trainer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fitness.trainer",
                    ),
                ),
            ],
        ),
    ]
