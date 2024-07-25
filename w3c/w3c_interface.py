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
gateway_map = { 10:'America', 20: 'Europe' }
gamemode_map = { 1: '1v1', 2:'2v2', 3:'3v3', 4:'4v4' }
race_map = { 1: 'Hu', 2: 'Or', 8: 'Ud', 4: 'Ne', 0: 'Rd' }
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

    @property
    def game_mode(self):
        return gamemode_map.get(self.gameMode)

    def opponents(self, battletag: str) -> list[MatchPlayer]:
        # collect teams which doesn't have this player on it.
        # collect players
        opponent_teams = []
        for team in self.teams:
            if not any([p.battleTag == battletag for p in team.players]):
                opponent_teams.append(team)

        return sum([
            team.players for team in opponent_teams
        ], []) if opponent_teams else []

    def describe(self, user_bt: str):
        oppos = self.opponents(user_bt)
        return (
            f"Map: {self.map} Time elapsed: {(self.startTime.replace(tzinfo=None) - datetime.now()).seconds} seconds",
            f"Oppo: { ', '.join(p.battleTag for p in oppos) }",
            f"Game M0de: {self.game_mode}"
        )
