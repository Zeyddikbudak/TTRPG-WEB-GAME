# Generated by Django 5.1.7 on 2025-05-06 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creature', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creature',
            name='armor_class',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='creature',
            name='hit_points',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
