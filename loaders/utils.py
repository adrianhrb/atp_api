import csv
from datetime import datetime

from matches.models import Match
from players.models import Player


def load_database_data(file, kind='M'):
    decoded_file = file.read().decode('utf-8').splitlines()
    reader = csv.DictReader(decoded_file)
    for row in reader:
        if kind == 'P':
            if row['birthdate'] != '':
                date = datetime.strptime(row['birthdate'], '%Y-%m-%d').date()
            Player.objects.create(
                player_id=row['player_id'],
                name=row['name'],
                hand=row['hand'],
                country=row['country'],
                birthdate=date,
            )
        else:
            if row['date'] != '':
                date = datetime.strptime(row['date'], '%Y-%m-%d').date()
            Match.objects.create(
                match_id=row['match_id'],
                tournament=row['tournament'],
                date=date,
                round=row['round'],
                duration=int(row['duration'].split('.')[0]),
            )


def assign_winners_and_losers(file):
    decoded_file = file.read().decode('utf-8').splitlines()
    reader = csv.DictReader(decoded_file)
    for row in reader:
        match = Match.objects.get(match_id=row['match_id'])
        player = Player.objects.get(player_id=row['player_id'])
        if row['winner'] == 'TRUE':
            match.winner = player
        else:
            match.loser = player
        match.save()
