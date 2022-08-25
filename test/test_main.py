import arkhamutilities.main
import arkhamutilities.db
import datetime


def validate_decklists_all_valid():
    raw_decklists = [
        arkhamutilities.db.Decklist(id=38616, create_date=datetime.datetime(2022, 8, 25, 14, 5, 34, 296168),
                                    update_date=datetime.datetime(2022, 8, 25, 14, 5, 34, 296168), version='1.0',
                                    xp=None,
                                    xp_spent=None, exile_string=None, taboo_id=4, tags='multiplayer, theme')]
    assert arkhamutilities.main.validate_decklists(raw_decklists) == raw_decklists
