# Generated by Django 5.0.1 on 2024-01-23 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0003_player_player_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='player_id',
        ),
        migrations.AlterField(
            model_name='player',
            name='id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]