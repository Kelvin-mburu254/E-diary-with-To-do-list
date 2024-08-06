# Generated by Django 4.2.6 on 2024-04-07 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("eDiary", "0005_alter_category_signup_alter_notes_signup_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notes",
            name="category",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="eDiary.category",
            ),
        ),
        migrations.AlterField(
            model_name="noteshistory",
            name="signup",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="eDiary.signup",
            ),
        ),
    ]
