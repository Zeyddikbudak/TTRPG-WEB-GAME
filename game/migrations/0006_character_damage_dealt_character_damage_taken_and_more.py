# Generated by Django 5.1.7 on 2025-06-01 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_character_is_temporary_character_melee_dice_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='damage_dealt',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='damage_taken',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='healing_done',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='kills',
            field=models.IntegerField(default=0),
        ),
    ]
