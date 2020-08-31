#!/usr/bin/env python3

from itertools import zip_longest
from operator import attrgetter

from elo_ratings import new_ratings
from players import Player

def round_one(players):
    """ This function takes a list of Player objects, and prints the first round pairing. In the first round of Monrad, the pairing is always the same.
    """

    print("\nDetermine round matches\n")

    ### This uses iterator approach to pairing items in a list
    paired = zip_longest(players[::2], players[1::2])
    zipped_paired = list(paired)

    for item in zipped_paired:
        if item[1] == None:
            print("Seed", item[0].seed, item[0].name, "gets a bye.")
            item[0].bye = True
            item[0].score += 1
        else:
            print("Seed", item[0].seed, item[0].name, "vs. Seed", item[1].seed, item[1].name)
            item[0].played.append(item[1].seed)
            item[1].played.append(item[0].seed)

    print()

def update_results(list_of_players):
    """This function is called at the end of each round and updates the score.
    """

    print("\nInput scores from matches\n")

    for player in list_of_players[::2]:
        # Remove players who got a bye
        if player.played == []:
            continue
        opponent = player.played[-1] - 1
        status = str.lower(input("Did seed {} {} win their match against seed {} {}? Y/N  ".format(player.seed, player.name, list_of_players[opponent].seed, list_of_players[opponent].name)))
        if status == "y":
            player.score += 1
        else:
            list_of_players[opponent].score += 1

    print("\nScoring complete\n\n")

def round_two(list_of_players):
    """This function sorts by the scores from the last round, then by the seed number, to pitch the most competitive players against each other - but only if they have not already played one another.
    """

    print("\nDetermine round matches\n")

    # Sorts players by score and by seed, so they can be paired
    s = sorted(list_of_players, key=attrgetter('seed'))
    s = sorted(s, key=attrgetter('score'), reverse=True)

    # Reuses the pairing logic from round one.
    paired = zip_longest(s[::2], s[1::2])
    zipped_paired = list(paired)

    for item in zipped_paired:
        if item[1] == None:
            print("Seed", item[0].seed, item[0].name, "gets a bye.")
            item[0].bye = True
            item[0].score += 1
        else:
            print("Seed", item[0].seed, item[0].name, "vs. Seed", item[1].seed, item[1].name)
            item[0].played.append(item[1].seed)
            item[1].played.append(item[0].seed)

    print("\nMatch list complete\n")
    return s

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

# TODO Handle the case where all or some players are unrated!

# Set seeding; likely a better way of doing this
# Seeding is permanent for the tournament
seed_rank = 1
for player in sorted_players:
    player.seed = seed_rank
    seed_rank += 1

# Print out first round matches and note who has played / got a bye
round_one(sorted_players)

update_results(sorted_players)

r2 = round_two(sorted_players)

for player in r2:
    print(player.name)

## TODO - the current issue is in this section somewhere; the following update_results seems to skip a round. If all odds win in the first round, then Timmy Whippet's second round should be against Waxy Pomelo. This is determined correctly, but when it requests input for the scores updating the prompt puts Timmy Whippet against seed 5 Griselda Nib. The next score it requests is Griselda Nib versus seed 13 Functional Glibro.

update_results(r2)

r3 = round_two(r2)


for player in sorted_players:
    print(player.seed, player.name, player.played, player.bye, player.score)
