# Generated by Django 4.2.11 on 2024-04-27 13:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("BE_table", "0008_alter_followupbe_username_field"),
    ]

    operations = [
        migrations.AlterField(
            model_name="followupbe",
            name="username_field",
            field=models.CharField(default="admin_jgp", max_length=25),
        ),
    ]