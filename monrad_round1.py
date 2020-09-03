#!/usr/bin/env python3

from itertools import zip_longest
from operator import attrgetter

from elo_ratings import new_ratings
from players import Player


def seed_players(list_of_players, rated=True):
    """After registration, players are sorted and seeded. The assumed case is that they have an Elo rating (rated=True). If they do not, they are sorted alphabetically by their names.
    """
    # If all players are not rated, should be sorted by name
    if rated == False:
        sorted_players = sorted(list_of_players, key=attrgetter('name'))
    # Sort players by starting Elo rating for initial seeding
    else:
        sorted_players = sorted(list_of_players, key=attrgetter('current_rating'), reverse=True)

    # Establish the players seed, based on their position in the initial sort
    seed_rank = 1
    for player in sorted_players:
        player.seed = seed_rank
        seed_rank += 1

    return sorted_players


def print_pairings(list_of_players, round_number):
    """ Helper function for rounds.
    Takes sorted list of Player objects in which players to play each other are
    in sequence, and zips through the list to print them out.
    """

    print('================= Round {} ================='.format(round_number))

    ### This uses iterator approach to pairing items in a list
    paired = zip_longest(list_of_players[::2], list_of_players[1::2])
    zipped_paired = list(paired)

    for item in zipped_paired:
        if item[1] == None:
            print("Seed", item[0].seed, item[0].name, "gets a bye.")
            item[0].bye = True
            item[0].score += 1 # Byes count as a win
        else:
            print("Seed", item[0].seed, item[0].name, "vs. Seed", item[1].seed, item[1].name)
            item[0].played.append(item[1].seed)
            item[1].played.append(item[0].seed)

    print()


def update_results(list_of_players):
    """This function is called at the end of each round and updates each Player's score.
    """

    print("\nInput scores from matches\n")

    opponent = 1 # Hacky, but designates opponents, in steps of two
    for player in list_of_players[::2]:
        # Remove players who got a bye
        if player.played == []: # This doesn't work; only works for the first round. Equally setting this to bye = True would remove each player as they got a bye.
            continue

        #opponent = player.played[-1] - 1 # This is the bug; it relies on seed numbers, not on position in the list of players.

        status = str.lower(input("Did seed {} {} win their match against seed {} {}? Y/N  ".format(player.seed, player.name, list_of_players[opponent].seed, list_of_players[opponent].name)))
        if status == "y":
            player.score += 1
        else:
            list_of_players[opponent].score += 1
        opponent += 2

    print("\n================= Scoring complete =================\n")


def sort_by_score(list_of_players):
    """Helper function that returns a list_of_players sorted by score, then by seed.
    """
    s = sorted(list_of_players, key=attrgetter('seed'))
    s = sorted(s, key=attrgetter('score'), reverse=True)

    print("================= Current Standings =================\n")
    for player in s:
        print(player.name, player.score)

    print()
    return s


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

#----------------------------------------------------------------------------


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
competitors = []
for player in players.items():
    p = Player(player[0], player[1])
    competitors.append(p)


print('================= Welcome =================')
print()
print("""This is a Monrad-paired Swiss tournament; it depends on Elo ratings for normal use.
If a minority of players don't have Elo ratings,start them at a rating of 800.
If a majority of players don't have Elo ratings, then seed them alphabetically instead.
""")


seeded = seed_players(competitors)
print_pairings(seeded, 1)
update_results(seeded)
r2 = sort_by_score(seeded)
print_pairings(r2, 2)
print(r2[0].name,r2[1].name, r2[2].name, r2[3].name)
update_results(r2)
r3 = sort_by_score(r2)
print_pairings(r3, 3)
update_results(r3)

## TODO Make this a loop or a function to accept either a default number of rounds or a specified number of rounds.


final = sort_by_score(r3)
for player in r3:
    print(player.seed, player.name, player.played, player.bye, player.score)
