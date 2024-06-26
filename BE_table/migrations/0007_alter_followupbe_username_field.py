# Generated by Django 4.2.11 on 2024-04-27 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("BE_table", "0006_alter_followupbe_holes_length"),
    ]

    operations = [
        migrations.AlterField(
            model_name="followupbe",
            name="username_field",
            field=models.ForeignKey(
                default="admin_jgp",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
