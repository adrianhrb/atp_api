from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from matches.models import Match
from players.api.serializers import PlayerSerializer
from players.models import Player

from .serializers import MatchSerializer


class MatchViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


class MatchWinnerView(APIView):
    queryset = Match.objects.all()

    def get(self, request, pk, format=None):
        match = self.queryset.get(pk=pk)
        player = get_object_or_404(Player, id=match.winner.id)
        serializer = PlayerSerializer(player)
        return Response(serializer.data)


class MatchLoserView(APIView):
    queryset = Match.objects.all()

    def get(self, request, pk, format=None):
        match = self.queryset.get(pk=pk)
        player = get_object_or_404(Player, id=match.loser.id)
        serializer = PlayerSerializer(player)
        return Response(serializer.data)
