# Generated by Django 5.0.1 on 2024-01-23 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0004_alter_match_loser_alter_match_winner'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='match_id',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
