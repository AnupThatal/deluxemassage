# Generated by Django 4.2.3 on 2024-02-23 13:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category", models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name="course",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("course_name", models.CharField(max_length=1000)),
                ("file_mainpic", models.FileField(upload_to="")),
                ("title", models.TextField(max_length=200)),
                ("Description", models.TextField()),
                ("quotes", models.TextField()),
                ("important_notes", models.TextField()),
                ("price", models.IntegerField()),
                ("pic1", models.FileField(upload_to="")),
                ("pic2", models.FileField(upload_to="")),
                (
                    "offers",
                    models.CharField(
                        blank=True, default="0", max_length=500, null=True
                    ),
                ),
                ("offers_date", models.DateField(blank=True, null=True)),
                ("subject_email", models.CharField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="email_subscription",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Trainer",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("trainer_name", models.CharField(max_length=150)),
                ("expertise", models.CharField(max_length=1000)),
                ("trainer_pic", models.FileField(upload_to="")),
                ("country", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=300)),
                ("location", models.CharField(max_length=300)),
                ("contact", models.CharField(max_length=20)),
                ("desc", models.TextField(blank=True, null=True)),
                ("Email", models.EmailField(max_length=150)),
                ("is_trainer", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nationality", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254)),
                ("firstname", models.CharField(max_length=200)),
                ("lastname", models.CharField(max_length=300)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Itemcart",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "purchase_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "total_price",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                ("is_purchased", models.BooleanField(default=False)),
                ("is_completed", models.BooleanField(default=False)),
                ("name", models.CharField(max_length=200)),
                ("country", models.CharField(max_length=200)),
                ("location", models.CharField(max_length=200)),
                ("Email", models.EmailField(max_length=200)),
                ("contact", models.CharField(blank=True, max_length=50, null=True)),
                ("quantity", models.CharField(blank=True, max_length=20, null=True)),
                ("Any_sepcial_request", models.TextField(blank=True, null=True)),
                (
                    "items",
                    models.ManyToManyField(related_name="course", to="fitness.course"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="course_buy",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("country", models.CharField(max_length=100)),
                ("puja_date", models.DateField()),
                ("Email", models.EmailField(max_length=254)),
                ("contact", models.CharField()),
                ("payment", models.CharField()),
                ("address", models.TextField(max_length=500)),
                ("message", models.TextField(default="")),
                (
                    "paid",
                    models.BooleanField(
                        choices=[(True, "Yes"), (False, "No")], default=False
                    ),
                ),
                (
                    "completed",
                    models.BooleanField(
                        choices=[(True, "Yes"), (False, "No")], default=False
                    ),
                ),
                (
                    "puja_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="fitness.course"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="course",
            name="trainer_name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="trainers_profile",
                to="fitness.trainer",
            ),
        ),
        migrations.AddField(
            model_name="course",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.CreateModel(
            name="blog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=1000)),
                ("top_content", models.TextField()),
                ("content", models.TextField()),
                ("important_notes", models.TextField()),
                ("main_pic1", models.FileField(upload_to="")),
                ("pic1", models.FileField(upload_to="")),
                ("pic2", models.FileField(upload_to="")),
                ("Date", models.DateField(blank=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fitness.category",
                    ),
                ),
                (
                    "username",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
