# README tournament-management-racket

## Preamble

I am a hobbyist programmer (in Python thus far), and so I am building this project in Python to accompany or illustrate or think through [how I am trying to implement it in Racket](https://github.com/lucasboulding/tournament-management-racket) (which I am trying to learn). After I hit a significant roadblock in making progress on the Racket version, I am putting together a Python version to think about the problems and how I would resolve them in Python in the hope that this will help to clarify my way forward in Racket. 


What I would like to make is a suite of simple tournament management tools. First I would build them to run through the command line, and then (maybe) through a GUI. There are two tools I would like to focus on: an Elo ratings system, and a Swiss tournament manager (using Monrad pairing). I have decided to develop both simultaneously because the Swiss-Monrad system depends on ratings for sustained use. 


I could try to make the tools "game agnostic", but one of the aims of this exercise is to learn to make a tailored system that responds to the eccentricities of a given game. To that end, I will be picking traditional pub card game Cribbage for the purposes of this project (specifically [six card cribbage](https://www.pagat.com/adders/crib6.html) for two players). It's a low-stakes game, and as far as I am aware there isn't a dedicated tournament solution available.


It would be nice to have a script that could accept a batch of results and calculate the resulting Elo ratings for a whole group of players (say, tournament results). Assuming a group of regular players, it would also be nice to have a way of permanently storing all the results and the current Elo rating for each player. If this project were to get more complicated, maybe it would be nice to share these (either by emailing the updated result, or by having a website which players could access to see their ratings).


## Installation

Currently this is not setup for usage by third parties. It is a basic Python script.

## Usage

These scripts assume that you have Python 3.8 installed.

### `ur_code_elo_rating.py`

Run this script from the terminal. It prompts the user to enter two players names, their existing Elo ratings, and then provide the possible Elo ratings changes outcomes from their match. 



## Contributing


## License

