

## Quick script to calculate Elo ratings of two players, using "logistic curve", like USCF


## Design notes: ** = to the power of
## This calculates Elo rating using a K factor of 32, appropriate to the lower levels of play. A higher level can use K 16 or at the highest levels K 10.


KFACTOR = 32



def expected_score(rating_a, rating_b):
    """
    This function takes two player ratings and returns the expected score of the first player against the second.
    The expected output is a decimal between 0 and 1, which can also be thought of as the probability of a victory.

    """
    QA = 10 ** (rating_a / 400)
    QB = 10 ** (rating_b / 400)
    expected_score = QA / (QA + QB)
    return(expected_score)


def update_rank(initial_rating, actual_score, expected_score):
    """
    This function takes a players initial rating, the actual score their match against an opponent, and the expected
    score of that match. It returns a new rating, which should have gone up if they won and down if they lost.
    """
    new_rank = initial_rating + KFACTOR * (actual_score - expected_score)
    return(round(new_rank))


def k_factor():
    # k = (natural-log(absolute(pointsdifference) + 1)) * (2.2 / ((winning team old elo rating - losing team old elo rating) * 0.001 + 2.2))
    pass




if __name__ == '__main__':
    # Establish player identity and existing rank:
    player_a_name = input("What is first player's name? ")
    player_b_name = input("What is second player's name? ")

    print()
    print("If a player doesn't have a rank, they begin on 800.")
    print()

    while True:
        try:
            player_a_initial = int(input(f"Please enter the rating of {player_a_name} as an integer: "))
            break
        except ValueError:
            print("Oops!  That was not a valid rating.  Try again...")


    while True:
        try:
            player_b_initial = int(input(f"Please enter the rating of {player_b_name} as an integer: "))
            break
        except ValueError:
            print("Oops!  That was not a valid rating.  Try again...")



    pa_expected = expected_score(player_a_initial, player_b_initial)
    print
    pb_expected = expected_score(player_b_initial, player_a_initial)

    print()
    print('Calculating expected scores...')
    print(f"{player_a_name}'s expected score:" + str(pa_expected))
    print(f"{player_b_name}'s expected score:" + str(pb_expected))



    print()
    print(f"If {player_a_name} lost...")

    pa_updated = update_rank(player_a_initial, 0, pa_expected)
    pb_updated = update_rank(player_b_initial, 1, pb_expected)

    print(f"{player_a_name}'s new rank is:" + str(pa_updated))
    print(f"{player_b_name}'s new rank is:" + str(pb_updated))


    print()
    print(f"If {player_b_name} lost:")

    pa_updated = update_rank(player_a_initial, 1, pa_expected)
    pb_updated = update_rank(player_b_initial, 0, pb_expected)

    print(f"{player_a_name}'s new rank is:" + str(pa_updated))
    print(f"{player_b_name}'s new rank is:" + str(pb_updated))



