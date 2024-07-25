import pytest
from w3c.players import Players
from w3c.player import Player
from w3c.w3c_interface import Match
from w3c.w3c_service import W3CApi, Endpoints, PlayerStats, re
from tools.environment import environment

@pytest.fixture
def players():
    return Players()


@pytest.fixture
def twitch():
    return "twitchuser"

@pytest.fixture
def bnet():
    return "SADROBOT#1797"

@pytest.mark.asyncio
async def test_add_remove_user(players: Players, twitch, bnet):
    environment.isMock = True

    await players.add_player(twitch, bnet)
    assert players[twitch]
    # remove based on channel name
    players.remove_player(twitch)
    # Second time should not work, already been removed
    assert not players.get(twitch)

@pytest.mark.asyncio
async def test_get_match(twitch, bnet):
    environment.isMock = True
    
    player = Player(twitch, bnet)
    match = player.get_current_match()
    assert type(match) is Match