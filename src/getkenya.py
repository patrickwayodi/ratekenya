# This is a program that selects the players from the Kenya federation.
# Note that this program uses about 1 GB of RAM to process the data.


import csv
import xml.etree.ElementTree as ET


tree = ET.parse("standard_nov25frl_xml.xml")


def count_all_players(players):

    total_players = 0

    for player in players:
        total_players = total_players + 1

    return total_players


def select_players_kenya(players):
    players_kenya = ET.Element(None)
    total_players = 0

    for player in players:
        for player_detail in player.iter('country'):
            if player_detail.text == "KEN":
                players_kenya.append(player)

    for player in players_kenya:
        for player_detail in player.iter('name'):
            print(player_detail.text)
        for player_detail in player.iter('rating'):
            print(player_detail.text)

    for player in players_kenya:
        total_players = total_players + 1

    players_kenya_xml_tree = ET.ElementTree(players_kenya)

    players_kenya_xml_tree.write(
        "players_kenya.xml",
        short_empty_elements=False,
        encoding="utf-8"
        )

    # Create a csv file
    # https://www.hellocodeclub.com/how-to-convert-xml-to-csv-in-python-step-by-step-guide
    csvfile = open("players_kenya.csv", 'w', encoding='utf-8')

    csvfile_writer = csv.writer(csvfile)

    # add the header to csv file
    csvfile_writer.writerow(["Name", "Rating", "FIDE ID", "Birthday", "Sex", "Country"])

    # for each player
    for player in players_kenya_xml_tree.findall("player"):
        if(player):
            # Extract the player details
            csv_line = [
                player.find("name").text,
                player.find("rating").text,
                player.find("fideid").text,
                player.find("birthday").text,
                player.find("sex").text,
                player.find("country").text
                ]
            # Add a new row to the csv file
            csvfile_writer.writerow(csv_line)

    return total_players


if __name__ == '__main__':

    chess_players = tree.getroot()

    print()

    # Total players in Kenya federation: 1170 (standard_jan25frl_xml.xml)
    # Total players in Kenya federation: 1373 (standard_nov25frl_xml.xml)
    print("Total players in Kenya federation:", select_players_kenya(chess_players))

    print()

    # Total players in the full list: 486934 (standard_jan25frl_xml.xml)
    # Total players in the full list: 524186 (standard_nov25frl_xml.xml)
    print("Total players in the full list:", count_all_players(chess_players))

    print()

    # sys.exit(main(sys.argv))

