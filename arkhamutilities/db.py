import enum
import sqlite3

from datetime import datetime
from sqlmodel import Field, create_engine, SQLModel, Enum, Column
from typing import Optional, List

sqlite_file_name = "arkham-utilities.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=True)


# todo create index

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


class Decklist(SQLModel, table=True):
    id: int = Field(primary_key=True)
    create_date: datetime
    update_date: datetime
    investigator_id: int
    version: str
    slots: List[int]
    side_slots: List[int]
    xp: Optional[int] = None
    xp_spent: Optional[int] = None
    exile_string: Optional[str] = None
    taboo_id: Optional[int] = None
    tags: Optional[str] = None

    # TODO future enhancement, create a table of decklist_id, card_id, count to store cards instead of slot csv
class Slots(enum.Enum):
    hand = 1
    hand2 = 2
    body = 3
    accessory = 4
    arcane = 5
    arcane2 = 6
    ally = 7


class PlayerCards(SQLModel, table=True):
    id: int = Field(primary_key=True)
    pack_code: str
    type_code: str
    faction_code: str
    exceptional: bool
    myriad: bool
    name: str
    cost: int
    quantity: int
    intellect: int
    combat: int
    agility: int
    wild: int
    deck_limit: int
    slot: Slots = Field(sa_column=Column(Enum(Slots)))
    traits: str
    is_unique: bool
    permanent: bool
class IdentityCards(SQLModel, table=True):
    id: int = Field(primary_key=True)
    pack_code: str
    type_code: str
    faction_code: str
    exceptional: bool
    myriad: bool
    name: str
    cost: int
    quantity: int
    intellect: int
    combat: int
    agility: int
    health: int
    sanity: int
