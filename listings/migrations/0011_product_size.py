# Generated by Django 3.0.4 on 2021-08-24 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0010_product_delivery_charges'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.BooleanField(default=False),
        ),
    ]