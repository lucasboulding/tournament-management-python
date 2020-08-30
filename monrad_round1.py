#!/usr/bin/env python3

from itertools import zip_longest
from operator import attrgetter

from elo_ratings import new_ratings
from players import Player

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
            #"Stefan Funke": 581,
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


sorted_copy = list(sorted_players)


match_number = 1
# while len(sorted_copy) != 0:
#     x,y = sorted_copy[:2]
#     print("Match number {} is between seed {} {} and seed {} {}".format(match_number, x.seed, x.name, y.seed, y.name))
#     x.played = x.played.append(y.seed)
#     y.played = y.played.append(x.seed)
#     sorted_copy.pop(0)
#     sorted_copy.pop(0)
#     match_number += 1

# for x in sorted_copy:
#     for y in sorted_copy:
#         print("Match number {} is between seed {} {} and seed {} {}".format(match_number, x.seed, x.name, y.seed, y.name))
### This solution works, but depopulates the list and doesn't return the
### seed information to the real object, only to the copy.

### This uses iterator approach
paired1 = zip_longest(sorted_copy[::2], sorted_copy[1::2])
zipped_paired1 = list(paired1)

for item in zipped_paired1:
    if item[1] == None:
        print("Seed", item[0].seed, item[0].name, "gets a bye.")
        item[0].bye = True
    else:
        print("Seed", item[0].seed, item[0].name, "vs. Seed", item[1].seed, item[1].name)
        item[0].played.append(item[1].seed)
        item[1].played.append(item[0].seed)


for player in sorted_players:
    print(player.seed, player.name, player.played, player.bye)
