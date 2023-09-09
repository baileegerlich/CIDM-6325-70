# Generated by Django 4.2.5 on 2023-09-09 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("name", models.CharField(help_text="Project Name", max_length=50)),
                (
                    "creation_time",
                    models.DateTimeField(
                        auto_now_add=True, help_text="Project creation time."
                    ),
                ),
                (
                    "completion_time",
                    models.DateTimeField(
                        help_text="Project completion time", null=True
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Task",
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
                ("title", models.CharField(help_text="Task title", max_length=100)),
                ("description", models.TextField(help_text="Task description")),
                (
                    "time_estimate",
                    models.IntegerField(
                        help_text="Time in hours required to complete the task."
                    ),
                ),
                (
                    "completed",
                    models.BooleanField(
                        default=False, help_text="Task completion status"
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="projectp.project",
                    ),
                ),
            ],
        ),
    ]
