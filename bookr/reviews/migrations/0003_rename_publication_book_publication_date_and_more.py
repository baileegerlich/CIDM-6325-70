# Generated by Django 4.2.5 on 2023-09-29 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0002_book_contributor_review_bookcontributor_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="book", old_name="publication", new_name="publication_date",
        ),
        migrations.AlterField(
            model_name="review",
            name="date_created",
            field=models.DateTimeField(
                auto_now_add=True, help_text="The date and time the review was created."
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="date_edited",
            field=models.DateTimeField(
                help_text="The date and time the review was last edited.", null=True
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="rating",
            field=models.IntegerField(help_text="The rating the reviewer has given."),
        ),
    ]
