---
author: Lucas Boulding
title: Design Process Log
date: 2020-06-13
---

# Preamble

This log outlines the thinking behind my code. This form of documentation can prove invaluable for troubleshooting, but it's primary function is to assist in my learning. In some senses it's like a verbose git commit, except that it includes my thinking process as well as actual technical detail. It will include theories about how I think things work, as well as plans, goals, attempts, and failures. Most recent log entry first, and each log entry is written in approximately chronological order as I proceed through a programming session.


# Style Guide

Terms:

- People who play the game = players
- People in the system = rated players
- People who take part in a tournament = competitors


# Log


## 2020-08-31

Wrote update score function; takes user input on whether player x beat player y to determine the score for player x and y.

Wrote the second round function, which is based on the sort stability trait described in the Python documentation. Went through three different sort approaches before arriving at this solution; see below:


```python
#This is from the O'Reilly Python Cookbook
 round_list = sorted(list_of_players, key=lambda x,y: (
cmp(player(x).score, player(y).score or  # Sort by score
cmp(player(x).seed, player(y).seed)))) # sort by seed
 print(round_list)
### This didn't work

aux_list = map(lambda x: (x, sorting_criterion_score(x),  sorting_criterion_seed(x)), list_of_players)
aux_list.sort(lambda x,y:
cmp(x[1], y[1]) or
cmp(x[2], y[2]))
round_list = map(lambda x: x[0], aux_list)
for player in round_list:
   print(player.name)
### This didn't work

list_of_players.sort(key = lambda player: (player.score, player.seed))
### This completes most of the sorting correctly, in that it divides in two and ranks by seed, but it sorts 0 points above 1 point, so need to rank the score descending. According to the writeup here (http://www.lleess.com/2013/08/python-sort-list-by-multiple-attributes.html) the only way to get the score to sort descending is to use a cmp function.

round_list = multi_sort(list_of_players, (('score', True), ('seed', True)))
```

The current outstanding issue is in the pairing logic for later rounds; it only asks about odd numbered players, not about the complete set of games. Not the pairing logic in fact, but the score updating logic. 




## 2020-08-30

This process is beset by confusion. Lack of clear specification is hampering my attempt, and lack of progress in the attempt is impinging on my motivation. So a different approach is necessary. Instead of worrying about all the IO, I'm just going to focus on learning the necessary logic to make basic steps. The first step of a Monrad-Swiss tournament is getting people through the door, taking their Elo ratings and sorting them. So I'll work out how to take a list of Elo ratings and sort it.

Started using a simple dictionary, sorted it. Then started using the Player class so that other features can also be recorded in the attributes, like initial seeding.

Set initial seeding, using the beginner's increment.

Now need to print initial match ups; given the sorting above, the pairing will always be the same.




## 2020-06-14

Okay, so based on my reasoning yesterday, what we need now is to divide off the Elo rating functions. Although I'm not really *au fait* with proper OOP, perhaps it would be sensible to make the Elo rating a class that could be imported from other scripts? But is it really complicated enough to warrant that? For updating a rating, what it needs is to know the winner's initial Elo rating, the loser's initial Elo rating, and which person won; from that, it should be able to return the winner's updated Elo rating and the loser's updated Elo rating. If the update function is positional, then using input like `def update(winner_elo, loser_elo)` should be enough, because the position reports the outcome of the match — in cribbage of course there cannot be a draw. If draws were possible, then it would be necessary to also input an `outcome` variable to calculate the updated ratings.


I'm thinking that we're going to be using pandas and numpy for this project, because the calculations are important and we might well need to interface with dataframes. However, it's not clear to me if Python's inbuilt maths operations are sufficiently accurate for this level of computation — my feeling is its probably fine.


So I've created a new script to house the ratings logic. I've created the function described above, now named `new_ratings(winner_elo, loser_elo)`, to be the "user facing" function. It uses the two other functions to return a list `[winner_updated, loser_updated]`, so just two round numbers. That should be easy to parse for further handling in the next script, and because the position of the updated information is the same it should be intuitive.


The next step is to work out how I am going to receive batches of match information. In my initial set of test data, `test_match_results.csv`, I've created one match for each player we're tracking. To some extent I've jumped the fun there, because I should really create a script that cretes Monrad pairings. To do that, I need to feed in a list of players and their Elo ratings. It would be sensible to feed it in in order, but let's imagine that I'm on the front desk of a walk-in tournament, and these players just rock up, give me their ratings, and then expect the computer to handle it. What it needs to do, then, is to get all that data, then sort it by Elo rating (and then alphabetically) and then...


Hmm. Maybe it would be better to think about this more long term off the bat. At some point it seems likely I'm going to need to create an object for each player in the system, maybe containing information like their name, their initial Elo rating, their initial seeding, their cumulative score in the tournament (for pairing each round), and a list of who they've already played. `player.py` In working this out, I see that I need more than this. There should be a base player class, which should list the player's most basic details (i.e. name, current Elo rating, a datestamp of their "joining the system", and maybe a history of tournaments they've played in).


Actually, maybe I need to revise my thinking on this. I want to both be able to simulate club play (i.e. normal matches played in a non-tournament structure at club meetups once a month) and Monrad tournaments. This reflects my specific use case. Assuming that tournaments are the more "prestigious" category, it would make sense to retain information about a player's participation in past tournaments (maybe also their places in those tournaments, tuple of tournament name/id and a rank?). Maybe I should work on establishing a method for recording and updating club play records first, then working on tournament records in the second phase (since the pairing and so on is more likely to be technically complex).


Thinking this through, what tools do I need for club play? I need a record of players and their current ratings. I need a record of the match results that come in, so that ratings can be updated accordingly - let's assume for the time being that they come in as some kind of paper sheet that the club secretary turns into a spreadsheet for further processing. Ultimately, a database would be the solution for this, but let's try something quick and dirty with a CSV first. What I think this would look like would be: a CSV containing the names and current Elo ratings of club members (maybe a club ID number would be sensible too); a CSV containing a new batch of match scores from one evening of club play (match ID, winner club ID, winner score, loser club ID, loser score) [on reflection, don't need winner score because it will always be 121]; another CSV containing the historic match records (datestamp, match ID, winner club ID, loser club ID, loser score). As a new batch is processed, the current ratings get updated, the new records are added to the historic records file, and the new batch of records is deleted (? bit severe; not if it works properly). Tweaking things a little as we go, those are now `current_players.csv`, `new_match_records.csv`, and `historic_match_records.csv` Match IDs clearly can't correspond to the order they're played in, because club play takes place simultaneously. Assuming that club play will also not be structured, i.e. random pairing, I will assign arbitrary identifiers (maybe based on the order the paper sheets are handed in?). To further distinguish match IDs, I've prefixed them M1, M2. Maybe player IDs should be prefixed P too? It helps with back office work to have easy ways of telling strings of numbers apart, even if it's not elegant. Makes it more human legible.


OK, I've made some progress. I've separated the ratings logic into a file. I've created a basic Player class. I've started to create a script for managing club play, which reads in the list of players and their current ratings into a list of Player objects. Now I am trying to work out how to batch process ratings changes (again, lets assume that the rating period is one month's club play). So what that entails is summing up each player's total score across the evening, and summing up their total projected score against each opponent they played. Then you perform the standard rating operation, replacing score and expected score with the total score and total expected score, which gives you the new rating. However, what I realise is that if I perform that operation on one player, that will change their rating when I move on to perform the operation on the next player, which will mean that according to the computer, the player will be playing against the first player's new rating, not the rating they had when they actually played one another. I thought I'd make a quick list of tuples of players and their initial ratings that I could always refer to, but this has proved difficult. Maybe I should just create another dictionary of scores that doesn't get modified so that it can be referred to without alteration?  





## 2020-06-13

I have started this parallel Python version of this project to illuminate my Racket learning journey. Hopefully this should be much more plain sailing, given my more advanced Python skills. I've started from a bit of code I wrote when I was trying to understand Elo ratings in general, `ur_code_elo_rating.py`, which is intended to be run from the command line. It walks through some prompts to get user input and to provide more user-friendly output, for instance associating names with player scores.


However, this clearly isn't suitable for larger purposes. The internal logic of the Elo ratings needs to be separated out from the "user-facing" portion, so that the Elo ratings functions can also be supplied to other scripts.


Let's start by reviewing the problem. When running a tournament that reflects the various design preferences in the Design Document (fair, fun, as many games for participants as possible, variety of opponents, evaluate a winner), and assuming a reasonably consistent pool of regular players, the Monrad Swiss system emerges as the best candidate for tournament play  — other systems may be better in other circumstances. In the Monrad system, each player has a rating, and the tournament is seeded according to those ratings. The first round pits the first seed against the second seed, the third against the fourth and so on. The results of the first round determine the next round of play; in Cribbage every game results in a winner and a loser, so excluding byes, half the field is a winner and half a loser (or put another way half the field will have a score of 1 and half a score of 0). These two fields are then listed according to their initial seedings, and then pairing proceeds to match the strongest against one another down the list. This process is used for all subsequent rounds, though of course after the second round there may be many more "groups" of scores, i.e. some who won, then lost. At the end of the first round, the only possible scores are 0 and 1. At the end of the second round, they can be 0, 1, 2. At the end of the third round they can be 0, 1, 2, 3. Etc.


So what tools do we need to make this work? Firstly, we need to have a way to reliably calculate Elo ratings to create the initial rating conditions. Secondly, we need to have a system that can do several types of pairing calculation; in the first round it needs to seed by Elo rating; in the second round and subsequent rounds it needs to seed by score (then Elo rating within score groups). At the end, it needs to return not only the results of the tournament, but the new Elo ratings for the players going forward.


Lets imagine that we join a club and there are some score sheets from previous tournaments that allow us to form a basic sense of the strength of the players, and perform the initial rankings. If we know something about the strengths of the players, maybe we could use one set of tournament results to set some approximate Elo ratings, and the remaining tournament results as input to add and decrease ratings accordingly. The official Elo method, 3.4. The Method of Successive Approximations, is more complex than necessary for our stimple league example. The second official method, where no previous information exists, is to set all players to the same rating and then adjust in subsequent play, using a large K factor (Elo recommends from 32 up to 50) to get the ratings to the right sort of levels. He does suggest setting up a round robin special rating tournament to increase the accuracy of the ratings.


Lets say that rather than Elo's methods, we use the one I've suggested, and we end up with the initial Elo ratings in `test_player_starting_values.csv`.
