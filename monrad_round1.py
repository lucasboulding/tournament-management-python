#!/usr/bin/env python3

from itertools import zip_longest
from operator import attrgetter

from elo_ratings import new_ratings
from players import Player

def round_one(players):
    """ This function takes a list of Player objects, and prints the first round pairing. In the first round of Monrad, the pairing is always the same.
    """
    ### This uses iterator approach to pairing items in a list
    paired = zip_longest(players[::2], players[1::2])
    zipped_paired = list(paired)

    for item in zipped_paired:
        if item[1] == None:
            print("Seed", item[0].seed, item[0].name, "gets a bye.")
            item[0].bye = True
        else:
            print("Seed", item[0].seed, item[0].name, "vs. Seed", item[1].seed, item[1].name)
            item[0].played.append(item[1].seed)
            item[1].played.append(item[0].seed)


# Arbitrary dict of players
players = {"Timmy Whippet": 1181,
            "Margo Bunt": 1089,
            "Waxy Pomelo": 1082,
            "Hugo Cockatrice": 1070,
            "Griselda Nib": 1058,
            "Jenny Frame": 1042,
            "Hooper Hibblethwaite": 1031,
            "Wandril Gudgeon": 910,
            "Vernon Mann": 906,
            "Craig Kassel": 882,
            "Jasmine Minge": 858,
            "Elsbeth Bethels": 756,
            "Functional Glibro": 713,
            "Patricia Partridge": 653,
            "Stefan Funke": 581,
            "Jim Dynamo": 410,}

# Transform dict into list of player objects
list_of_players = []
for player in players.items():
    p = Player(player[0], player[1])
    list_of_players.append(p)

# Sort players by starting Elo rating for initial seeding
sorted_players = sorted(list_of_players, key=attrgetter('current_rating'), reverse=True)

# Set seeding; likely a better way of doing this
# Seeding is permanent for the tournament
seed_rank = 1
for player in sorted_players:
    player.seed = seed_rank
    seed_rank += 1

# Print out first round matches and note who has played / got a bye
round_one(sorted_players)



for player in sorted_players:
    print(player.seed, player.name, player.played, player.bye)
