import datetime
import pandas as pd
import requests
import db


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

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


# makes a request to https://arkhamdb.com/api/public/decklists/by_date/ for each date in the range
def request_decklists_by_date_range(from_date: datetime.date, to_date: datetime.date):
    for single_date in pd.date_range(from_date, to_date):  # TODO replace code if don't want to use pandas elsewhere
        print(single_date)
        # request_decklists_by_date(single_date)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    db.initialize()
    request_decklists_by_date_range(datetime.datetime(2022, 8, 1), datetime.date.today())
