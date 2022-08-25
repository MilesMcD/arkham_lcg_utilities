from arkhamutilities.db import Decklist
from arkhamutilities import main
import datetime


def test_validate_decklists_all_valid():
    raw_decklists = [
        Decklist(id=38616, create_date=datetime.datetime(2022, 8, 25, 14, 5, 34, 296168),
                 update_date=datetime.datetime(2022, 8, 25, 14, 5, 34, 296168), version='1.0',
                 xp=None,
                 xp_spent=None, exile_string=None, taboo_id=4, tags='multiplayer, theme')]
    assert main.validate_decklists(raw_decklists) == raw_decklists
