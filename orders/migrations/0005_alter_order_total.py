# Generated by Django 5.0.3 on 2024-06-10 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_rename_user_order_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.FloatField(blank=True, null=True),
        ),
    ]