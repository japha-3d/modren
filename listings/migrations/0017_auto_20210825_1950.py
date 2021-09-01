# Generated by Django 3.0.4 on 2021-08-25 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0016_auto_20210825_1705'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='black',
            new_name='color1',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='blue',
            new_name='color2',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='green',
            new_name='color3',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='orange',
            new_name='color4',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='pink',
            new_name='color5',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='purple',
            new_name='color6',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='red',
            new_name='color7',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='white',
            new_name='color8',
        ),
        migrations.RemoveField(
            model_name='product',
            name='yellow',
        ),
        migrations.AddField(
            model_name='product',
            name='color9',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='color_1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='color_2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='color_3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='color_4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='color_5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='color_6',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='color_7',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='color_8',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='color_9',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]