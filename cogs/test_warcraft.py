import pytest
from bot import TwitchBot

@pytest.fixture
def test_bot() -> TwitchBot:
    yield TwitchBot()

def test_register_user(test_bot: TwitchBot):
    test_bot.get_channel('')
