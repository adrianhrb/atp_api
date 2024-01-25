from .models import Match

def build_custom_prompt(match: Match) -> str:
    winner = match.winner.name
    loser = match.loser.name
    tournament = match.tournament
    text = f'Make an overview of the last tennis match in {tournament}, where {winner} and {loser} played. The winner of the match was {winner} and loser was {loser}. The response must be smaller than 100 tokens'
    return text
