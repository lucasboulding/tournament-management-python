

# This script holds the Elo ratings calculations, which are then accessed by other scripts as necessary. 


"""
KFACTOR is a global variable that determines how much players ratings change after matches.
Where Elo ratings are long established and the games are primarily ones of skill, 
these ratings should not change much with each game played, so the KFACTOR should be low.
For instance, some high level play uses K 16 or even K 10. 
Where Elo ratings are new, or where there is more variation and chance involved, 
these ratings should change more to reflect this, and this means the KFACTOR should be high.
32 is a standard rating, and I will use that here. For rating new players, Elo (3.3) recommends
setting the KFACTOR between 32 and 50.
"""

KFACTOR = 32

"""
Should I want to do any exploratory modifications to KFACTOR, they should be worked out here.
"""




def expected_score(rating_a, rating_b):
    """
    This function takes two player ratings and returns the expected score of the first player against the second.
    The expected output is a decimal between 0 and 1, which can also be thought of as the probability of a victory.
    """
    QA = 10 ** (rating_a / 400)
    QB = 10 ** (rating_b / 400)
    expected_score = QA / (QA + QB)
    return(expected_score)


def update_rating(initial_rating, actual_score, expected_score):
    """
    This function takes a players initial rating, the actual score their match against an opponent, and the expected
    score of that match. It returns a new rating, which should have gone up if they won and down if they lost.
    """
    new_rank = initial_rating + KFACTOR * (actual_score - expected_score)
    return(round(new_rank))


def new_ratings(winner_elo, loser_elo):
    """
    This function is the "user" facing function, which takes the winner and loser's ratings,
    assuming no ties are possible, and returns the two updated ratings.
    """
    winner_expected = expected_score(winner_elo, loser_elo)
    loser_expected = expected_score(loser_elo, winner_elo)
    winner_updated = update_rating(winner_elo, 1, winner_expected)
    loser_updated = update_rating(loser_elo, 0, loser_expected)
    return([winner_updated, loser_updated])

