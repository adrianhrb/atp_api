# Generated by Django 5.0.1 on 2024-01-23 14:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0003_alter_match_loser_alter_match_winner'),
        ('players', '0002_alter_player_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='loser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lost_matches', to='players.player'),
        ),
        migrations.AlterField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='won_matches', to='players.player'),
        ),
    ]