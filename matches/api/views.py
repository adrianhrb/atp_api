from rest_framework import viewsets

from rest_framework.views import APIView
from rest_framework.response import Response

from matches.models import Match
from django.shortcuts import get_object_or_404

from .serializers import MatchSerializer


class MatchViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

# class MatchWinnerView(APIView):
#     def get(self, request, pk, format=None):
#         winer = 