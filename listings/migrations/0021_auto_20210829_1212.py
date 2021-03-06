# Generated by Django 3.0.4 on 2021-08-29 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0020_auto_20210826_0649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='original',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='percentage',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='volume',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
