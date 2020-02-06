# Generated by Django 3.0.2 on 2020-02-06 07:52

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sspanel", "0029_auto_20200131_0901"),
    ]

    operations = [
        migrations.AddField(
            model_name="ssnode",
            name="enlarge_scale",
            field=models.DecimalField(
                decimal_places=2,
                default=Decimal("1.00"),
                max_digits=10,
                verbose_name="倍率",
            ),
        ),
        migrations.AddField(
            model_name="vmessnode",
            name="enlarge_scale",
            field=models.DecimalField(
                decimal_places=2,
                default=Decimal("1.00"),
                max_digits=10,
                verbose_name="倍率",
            ),
        ),
    ]
