import csv

from elo_ratings import new_ratings
from players import Player


# Open data for reference and working
#players_list = pd.read_csv('current_players.csv')
#historic_matches = pd.read_csv('historic_match_records.csv')
#new_matches = pd.read_csv('new_match_records.csv')


# Import players from CSV records

players = {}

with open('current_players.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=";", quotechar='"')
    for row in csv_reader:
        players.update({row["player_ID"]: Player(row["player_ID"], row["player"], row["current_elo"])})

# Creates a dictionary of Player objects, key is player_ID.
# Player objects have player_ID, name, current_rating
# Therefore attributes can be accessed as players["player_ID"].attribute

print(players["8000"].current_rating)

period_static_ratings = []

for player in players:
    period_static_ratings.append((player["name"], player["current_rating"]))


print(period_static_ratings)


