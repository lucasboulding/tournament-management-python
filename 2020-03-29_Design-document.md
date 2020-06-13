---
author: Lucas Boulding
title: Swiss Tournament Manager
---


# Preamble

What I want to try to do here is to create a piece of software that I could use to create a tournament with the following ambitions or constraints: 

- **Fair to all participants**: this means that they play the opponents closest to them in skill
- **Fun for all participants**: this means that players get exciting games in which either could win
- **As many games for each player as possible**: rather than eliminate players, all players should get to continue to play until the tournament ends
- **Variety of games**: each participant should play each other participant no more than once. 
- **Evaluate a winner**: the tournament should result in a winner, and a ranking of all other players

This, it seems to me, is what constitutes the definition of a friendly tournament, one where the majority of participants get to play the game they like, get good matches in, improve through practice, and determine where they fall within the group. In this tournament, everyone stands to gain by playing.


This whole thing is a learning exercise. Firstly, I should aim to get them to run from DrRacket. Then maybe a command line utility, and then (maybe) a GUI to run it. That would be great. There are two tools I would like to focus on: an Elo ratings system, and a Swiss tournament manager (using Monrad pairing). I could try to make the tools "game agnostic", but one of the aims of this exercise is to learn to make a tailored system that responds to the eccentrities of a given game. To that end, I will be picking traditional pub card game Cribbage for the purposes of this project (specifically [six card cribbage](https://www.pagat.com/adders/crib6.html) for two players). It's a low-stakes game, and as far as I am aware there isn't a dedicated tournament solution available. It also has some unusual scoring features ("skunking") which could be used to make the Elo rating system more interesting. 



# Assumptions

Basic: 

- The tournament manager is embedded in a community of players who are interested in tournament-type play, so are happy to share their match information with the manager. 
- Matches in six card cribbage are 1 vs 1, and I will not deal with the variants for teams of paired players or with three players.
- The outcomes of matches are wins (worth 1 point) or losses (worth 0); there are no ties.
- Each competitor will be rated, using a simple implementation of the Elo system. Ratings should be persistent, so that if a player competes in multiple tournaments the accuracy of their rating is improved.
- The program is intended to work for rated players; however, if ratings are not available for any players, then the players should be seeded into random order. Should some players have a rating and some not, new players should be seeded at a rating of 800. Should there be any ties in rating, players should be seeded alphabetically. 
- There can be an even or odd number of competitors in the tournament. If there are an odd number in a round, then the lowest rated player will be given a bye. No player will receive more than one bye. 
- Competitors should be able to drop out of the tournament as play proceeds, and be added back in (it's a pub game, after all). Decisions to allow competitors to drop out and return should be made by tournament organisers, and the system should be able to implement their decision either way — maybe at a serious competition if you have to leave you can't rejoin, but in a more casual competition you might be allowed to jump back in. 


I will be implementing my current understanding of the Monrad pairing system, used by a number of Nordic Chess federations, though there are limited English language resources on this form of pairing, and this implementation may depart from the systems used in those federations. The Monrad pairing system always matches the closest skilled pair that it can, starting from the highest rated seed. That means that in the first round the pairings will be as follows: 1 v 2, 3 v 4, 5 v 6, ... n v n+1. This is seen as a weakness by some, who want the tournament to "build up" to the big clash between the top two rated seeds. However, all seeds will get closer games throughout the tournament if they are always matched to those closest to their skill level, meaning that play throughout the tournament should be more exciting for most players and for most spectators. 



There should be a minimum number of competitors in a tournament — call it five. 

Ideally it would be great to have player data persist, so that we could look at their performance over several tournaments. 

## Elo ratings tool 







## Monrad-paired Swiss Tournament tool


