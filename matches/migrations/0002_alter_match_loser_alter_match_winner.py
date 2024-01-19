# Generated by Django 5.0.1 on 2024-01-19 15:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0001_initial'),
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='loser',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='lost_matches', to='players.player'),
        ),
        migrations.AlterField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='won_matches', to='players.player'),
        ),
    ]