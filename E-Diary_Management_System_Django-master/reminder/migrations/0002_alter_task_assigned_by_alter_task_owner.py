# Generated by Django 4.1.7 on 2023-10-21 09:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("reminder", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="assigned_by",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="item_assigned",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="owner",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="item_created",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
