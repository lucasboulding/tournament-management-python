---
author: Lucas Boulding
title: Design Process Log
date: 2020-06-13
---

# Preamble

This log outlines the thinking behind my code. This form of documentation can prove invaluable for troubleshooting, but it's primary function is to assist in my learning. In some senses it's like a verbose git commit, except that it includes my thinking process as well as actual technical detail. It will include theories about how I think things work, as well as plans, goals, attempts, and failures. Most recent log entry first, and each log entry is written in approximately chronological order as I proceed through a programming session. 

# Log


## 2020-06-13

I have started this parallel Python version of this project to illuminate my Racket learning journey. Hopefully this should be much more plain sailing, given my more advanced Python skills. I've started from a bit of code I wrote when I was trying to understand Elo ratings in general, `ur_code_elo_rating.py`, which is intended to be run from the command line. It walks through some prompts to get user input and to provide more user-friendly output, for instance associating names with player scores.


However, this clearly isn't suitable for larger purposes. The internal logic of the Elo ratings needs to be separated out from the "user-facing" portion, so that the Elo ratings functions can also be supplied to other scripts. 

