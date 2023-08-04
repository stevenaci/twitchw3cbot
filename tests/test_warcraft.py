import pytest
from w3c.players import players, Player

@pytest.mark.asyncio
async def test_add_remove_user():
    # add a real player
    twitch = "protectionfromblue"
    bnet = "NWILLIAMS28#1797"
    assert await players.add_player(twitch, bnet)
    # remove based on channel name
    assert players.remove_player(twitch)
    # Second time should not work, already been removed
    assert not players.remove_player(twitch)


@pytest.mark.asyncio
async def test_current_match():
    player = Player("d", "Potholderz#11253")
    print(player.get_current_match().describe(player.bnet))
    