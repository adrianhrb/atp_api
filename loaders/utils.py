import redis
import csv
from datetime import datetime

from matches.models import Match
from django.conf import settings
from players.models import Player

# connection to redis
r = redis.Redis(host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                db=settings.REDIS_DB)

def load_players(file):
    decoded_file = file.read().decode('utf-8').splitlines()
    reader = csv.DictReader(decoded_file)
    for row in reader:
        if row['birthdate'] != '':
            date = datetime.strptime(row['birthdate'], '%Y-%m-%d').date()
        new_player = Player.objects.create(
            name=row['name'],
            hand=row['hand'],
            country=row['country'],
            birthdate=date,
        )
        r.set(row['player_id'], new_player.id) 
        new_player.save
        
def load_matches(file):
    decoded_file = file.read().decode('utf-8').splitlines()
    reader = csv.DictReader(decoded_file)
    for row in reader:
        if row['date'] != '':
            date = datetime.strptime(row['date'], '%Y-%m-%d').date()
        new_match = Match.objects.create(
            tournament=row['tournament'],
            date=date,
            round=row['round'],
            duration=int(row['duration'].split('.')[0]),
        )
        r.set(row['match_id'], new_match.id)

def assign_winners_and_losers(file):
    decoded_file = file.read().decode('utf-8').splitlines()
    reader = csv.DictReader(decoded_file)
    for row in reader:
        match_id = r.get(row['match_id'])
        player_id = r.get(row['player_id'])
        match = Match.objects.get(id=match_id)
        player = Player.objects.get(id=player_id)
        if row['winner'] == 'TRUE':
            match.winner = player
        else:
            match.loser = player
        match.save()
