from rest_framework import serializers

from matches.models import Match
from players.api.serializers import PlayerSerializer


class MatchSerializer(serializers.ModelSerializer):
    winner = PlayerSerializer(read_only=True)
    loser = PlayerSerializer(read_only=True)

    class Meta:
        model = Match
        fields = ['tournament', 'date', 'round', 'duration', 'winner', 'loser']
