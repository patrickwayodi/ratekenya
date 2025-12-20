import json
import xml.etree.ElementTree as ET

from datetime import date
from datetime import timedelta
from zipfile import ZipFile


def player_total(file_name):

    players_kenya = ET.Element(None)

    # https://stackoverflow.com/questions/67833208/zipfile-zipfile-extractall-missing-required-argument-self
    rating_list_zipped = ZipFile(file_name, "r")

    rating_list = rating_list_zipped.read(file_name[:-4] + ".xml")

    # https://docs.python.org/3.11/library/xml.etree.elementtree.html
    players = ET.fromstring(rating_list)

    total = 0

    for player in players:
        total = total + 1

    for player in players:
        for player_detail in player.iter('country'):
            if player_detail.text == "KEN":
                players_kenya.append(player)

    total_kenya = 0

    for player in players_kenya:
        total_kenya = total_kenya + 1

    return {"File": file_name, "Total": total, "Total Kenya": total_kenya}


def altdate(rating_date):

    dates = {
        "2015-12-01": "dec15",
        "2016-12-01": "dec16",
        "2017-12-01": "dec17",
        "2018-12-01": "dec18",
        "2019-12-01": "dec19",
        "2020-12-01": "dec20",
        "2021-12-01": "dec21",
        "2022-12-01": "dec22",
        "2023-12-01": "dec23",
        "2024-12-01": "dec24",
        "2025-12-01": "dec25",
    }

    alt_date = dates[rating_date]

    return alt_date


def gettotals():

    list_totals = dict()

    rating_date = date.fromisoformat("2015-12-01")

    i = 0
    # while i < 11:
    while i < 11:
        print(rating_date)
        list_totals[rating_date.isoformat()] = player_total("standard_"+altdate(rating_date.isoformat())+"frl_xml.zip")
        rating_date = date.fromisoformat(str(rating_date.year+1) + "-12-01")
        i = i + 1

    with open('rating-list-stats.json', 'w') as f:
        f.write(json.dumps(list_totals, indent=4))

    return list_totals


def getdate(date):

    return date


def subtract_dates(date1, date2):
    # https://docs.python.org/3/library/datetime.html#date-objects

    date1 = date.fromisoformat(date1)

    date2 = date.fromisoformat(date2)

    result = date2 - date1

    return result


def extract_zipped_file():

    # https://stackoverflow.com/questions/67833208/zipfile-zipfile-extractall-missing-required-argument-self
    data = ZipFile("standard_frl_xml.zip", "r")

    # file_content = ZipFile.read(data)
    file_content = data.read("standard_frl_xml.xml")

    return file_content


def getsize():

    with open("standard_frl_xml.zip", "rb") as f:
        data = f.read()
        # print(data)

    file_size = 0

    return file_size


def extract_zip(input_zip):
    #https://stackoverflow.com/questions/10908877/extracting-a-zipfile-to-memory

    input_zip=ZipFile(input_zip)

    return {name: input_zip.read(name) for name in input_zip.namelist()}


if __name__ == '__main__':

    print("\nStats")
    print("=====")

    print("\nThe date is:", getdate("2025-12-01"))

    print("\nThe interval is:", subtract_dates("2024-12-01", "2025-12-01"))

    print("\nPlayer totals:\n", gettotals())

    print("\n\n")

    # sys.exit(main(sys.argv))

