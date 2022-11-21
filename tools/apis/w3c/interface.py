from datetime import datetime
from typing import Optional
from pydantic import BaseModel

"""
{'map': 'amazonia', 'id': '5f40632b4521d79a2975cd8d', 'durationInSeconds': 0,
'startTime': '2020-08-22T00:13:04.235+00:00', 'endTime': '0001-01-01T00:00:00+00:00',
'gameMode': 1, 'teams': [
    {'players': [{'race': 4, 'oldMmr': 2066, 'currentMmr': 0,
'battleTag': 'walterelfo#1110', 'name': 'walterelfo', 'mmrGain': -2066, 'won': False,
'location': 'CL', 'country': None}], 'won': False
},
{'players': [{'race': 1, 'oldMmr': 2095, 'currentMmr': 0, 'battleTag': 'Fish#14989', 'name': 'Fish', 'mmrGain': -2095, 'won': False, 'location': 'SG', 'country': 'Kuwait'}], 'won': False}],
'gateWay': 10, 'season': 0}
https://statistic-service.w3champions.com/api/players/Minigun%2311620/winrate?season=2
"""

class WinLosses(BaseModel):
    race: int
    wins: int
    losses: int
    games: int
    winrate: float


class iPlayerAka(BaseModel):
    name: str
    main_race: str
    country: str
    liquipedia: str


class PlayerStats(BaseModel):
    battleTag: str
    name: str
    participatedInSeasons: list
    winLosses: list[WinLosses]


class MatchPlayer(BaseModel):
    race: Optional[int]
    oldMmr: Optional[int]
    currentMmr: int
    battleTag: str
    name: str
    mmrGain: int
    won: bool
    location: str
    country: Optional[str]

class MatchTeam(BaseModel):
    players: list[MatchPlayer]

class Match(BaseModel):
    map: str
    id: str
    durationInSeconds: int
    startTime: datetime
    endTime: datetime
    gameMode: int
    teams: list[MatchTeam]
    gateWay: int
    season: int

