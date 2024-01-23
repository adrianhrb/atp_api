from django.db import models

from players.models import Player


class Match(models.Model):
    match_id = models.CharField(max_length=255)
    tournament = models.CharField(max_length=255)
    date = models.DateField()
    round = models.CharField(max_length=255)
    duration = models.IntegerField()
    winner = models.ForeignKey(
        Player, related_name='won_matches', on_delete=models.CASCADE, blank=True, null=True
    )
    loser = models.ForeignKey(
        Player, related_name='lost_matches', on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self) -> str:
        return self.match_id
