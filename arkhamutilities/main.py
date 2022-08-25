import datetime

from sqlmodel import Session, select

import pandas as pd
import requests

from arkhamutilities.db import Decklist, engine, create_db_and_tables


# Grabs decks from a given date and returns them as a dictionary
def request_decklists_by_date(date: datetime.date):
    url = "https://arkhamdb.com/api/public/decklists/by_date/{0}-{1}-{2}".format(
        date.year, str(date.month).zfill(2), str(date.day).zfill(2)
    )
    print(url)
    response = requests.get(url)
    print(response)
    print(response.json())
    return response.json()


# Makes a request to https://arkhamdb.com/api/public/decklists/by_date/ for each date in the range
def request_decklists_by_date_range(from_date: datetime.date, to_date: datetime.date):
    for single_date in pd.date_range(
            from_date, to_date
    ):  # TODO replace code if don't want to use pandas elsewhere
        print(single_date)
        data = request_decklists_by_date(single_date)
        raw_decklists = [Decklist(**kwargs) for kwargs in data]
        validated_decklists = validate_decklists(raw_decklists)
        session.add_all(validated_decklists)
        session.commit()


def validate_decklists(decklists: [Decklist]) -> [Decklist]:
    print(decklists)
    return filter(lambda decklist: decklist.validate(), decklists)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    create_db_and_tables()
    session = Session(engine)
    request_decklists_by_date_range(
        datetime.datetime(2022, 8, 15), datetime.datetime(2022, 8, 16)
    )  # datetime.date.today())
    with session as session:
        decklists = select(Decklist)
        print("saved decklists", decklists)
