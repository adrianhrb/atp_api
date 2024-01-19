import csv
from datetime import datetime

from matches.models import Match
from players.models import Player


def load_database_data(file, kind='M'):
    decoded_file = file.read().decode('utf-8').splitlines()
    reader = csv.DictReader(decoded_file)
    for row in reader:
        if row['birthday'] != '':
            date = datetime.strptime(row['birthday'], '%Y-%m-%d').date()
        if kind == 'P':
            if row['birthday'] != '':
                date = datetime.strptime(row['birthday'], '%Y-%m-%d').date()
            Player.objects.create(
                name=row['name'], hand=row['hand'], country=row['country'], birthdate=date
            )
        else:
            if row['date'] != '':
                date = datetime.strptime(row['birthday'], '%Y-%m-%d').date()
            Match.objects.create(
                tournament=row['tournament'],
                date=date,
                round=row['round'],
                duration=int(row['duration']),
            )
    return print('Todo ok')


def assign_winners_and_losers(file):
    decoded_file = file.read().decode('utf-8').splitlines()
    reader = csv.DictReader(decoded_file)
    for row in reader:
        match = Match.objects.get(id=row['match_id'])
        player = Player.objects.get(id=row['player_id'])
        if bool(row['winner']):
            match.winner = player
        else:
            match.loser = player
        match.save()
    return print('Todo ok')
