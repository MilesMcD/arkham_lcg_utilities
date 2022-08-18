import datetime
import pandas as pd
import requests
import db
import json


# Grabs decks from a given date and returns them as a dictionary
def request_decklists_by_date(date: datetime.date):
    url = "https://arkhamdb.com/api/public/decklists/by_date/{0}-{1}-{2}".format(
        date.year,
        str(date.month).zfill(2),
        str(date.day).zfill(2)
    )
    print(url)
    response = requests.get(url)
    print(response)
    print(response.json())
    return response.json()

# Makes a request to https://arkhamdb.com/api/public/decklists/by_date/ for each date in the range
def request_decklists_by_date_range(from_date: datetime.date, to_date: datetime.date):
    all_decklists = []
    for single_date in pd.date_range(from_date, to_date):  # TODO replace code if don't want to use pandas elsewhere
        print(single_date)
        all_decklists.add(request_decklists_by_date(single_date))
    return all_decklists

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    db.initialize()
    request_decklists_by_date_range(datetime.datetime(2022, 8, 1), datetime.datetime(2022, 8, 5)) #datetime.date.today())
