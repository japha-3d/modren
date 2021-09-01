# Generated by Django 3.0.4 on 2021-08-25 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0015_auto_20210825_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='original',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='percentage',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]