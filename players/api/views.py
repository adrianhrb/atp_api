from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from players.models import Player

from .serializers import PlayerSerializer


class PlayerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class PlayerByName(ListAPIView):
    serializer_class = PlayerSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        return Player.objects.filter(name__icontains=name)


class PlayerByCountry(ListAPIView):
    serializer_class = PlayerSerializer

    def get_queryset(self):
        country = self.kwargs['country']
        return Player.objects.filter(country__icontains=country)
