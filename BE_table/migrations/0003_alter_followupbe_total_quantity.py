# Generated by Django 4.2.11 on 2024-04-25 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BE_table', '0002_followupbe_total_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followupbe',
            name='total_quantity',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
