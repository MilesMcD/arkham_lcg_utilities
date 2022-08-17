import sqlite3


def initialize():
    con = sqlite3.connect('arkham-utilities.db')
    create_decklist_table(con.cursor())


def create_decklist_table(c):
    c.execute('''
        CREATE TABLE IF NOT EXISTS decklists (
            [id] INTEGER PRIMARY KEY, 
            [create_date] DATETIME NOT NULL,
            [update_date] DATETIME NOT NULL,
            [investigator_id] INTEGER NOT NULL,
            [version] TEXT NOT NULL,
            [slots] TEXT NOT NULL,
            [side_slots] TEXT NOT NULL,
            [xp] INTEGER,
            [xp_spent] INTEGER,
            [exile_string] TEXT,
            [taboo_id] INTEGER,
            [tags] TEXT
        )
    ''')

    c.execute('''
        CREATE INDEX IF NOT EXISTS idx_investigator_id on decklists (investigator_id) 
    ''')

    # TODO future enhancement, create a table of decklist_id, card_id, count to store cards instead of slot csv