---
author: Lucas Boulding
title: Design Process Log
date: 2020-04-21
---

# Preamble

This log outlines the thinking behind my code. This form of documentation can prove invaluable for troubleshooting, but it's primary function is to assist in my learning. In some senses it's like a verbose git commit, except that it includes my thinking process as well as actual technical detail. It will include theories about how I think things work, as well as plans, goals, attempts, and failures. Most recent log entry first, and each log entry is written in approximately chronological order as I proceed through a programming session. 

# Log


## 2020-05-03 

I've been working my way through some basic testing with Racket IO, and I still find it counter-intuitive. I've managed to create a basic text file and get Racket to append basic text immediately where the last text left off. I worked my way through the documentation, and I think that `call-with-output-file` is the best fit for my case. It took me several attempts to get this to work — I had problems working out the role of the lambda function, where the "out" variable was coming from, and then getting it to actually save the file. 


Then I've managed to open my file of match results in Racket using the symmetrical `call-with-input-file`. Initially I used `read-string` because that was in the example function, but `read-line` makes more sense in this case. So far I can only make it print the first line, which is the header for the CSV file. 


I can see that we're skirting on the edge of another big topic here. If I were in this situation in Python, what I would be looking to do is to create a loop to go through every line in the file, but I know that's not how things are supposed to work in more functional languages. I suspect that what I need here is recursion, which, as I understand it at this point, is like a for loop in that it performs some transformation on each item in a list of values until it reaches some end point. I believe that it does this in pairwise fashion, by which I mean instead of processing a whole list it takes the first item on the list and processes, and the function returns a call to itself on the rest of the original list. As yet I do not understand why this is considered to be so brilliant, which is more than likely a classic example of the Dunning-Kruger effect. 


I looked at the csv-reading library by Neil Van Dyke, but this adds another layer of Racket complexity — namely, downloading and working with another library. So far, I've only worked with the core libraries. However, I see that the basic approach taken by Van Dyke is to transform the read-in lines into a list (I suspect it's a list of lists, but I'm not sure). 


Rather than re-invent the wheel, I'm going with csv-reading. I googled it, and using DrRacket's package manager, and the "do what I mean" tab, I installed csv-reading and its two dependencies, overeasy and mcfly. That appeared to work without a hitch. So I know a bit about CSVs, and I see that this library uses Reader Specs as a way of parsing out the various formats and dialects for CSVs that exist. By default it reads any one or more line-feed and carriage return characters as a new line. It uses `,` as the default separator (I usually prefer to use `;`), and by default it uses `"` as the field delimiter. 


Using this, I managed to get it to read in multiple lines (using the `next-row` function described in the documentation) and then read in the whole file as a list (using the `csv->list` function). What would be necessary now would be to extract this information from the list to feed it into the Elo rating changes function. 


### Later on 1903

I've just been reading over the basics in _Realm of Racket_ and making notes, to try to make sure I've got enough of a handle on the basics. As I made notes on structures, I see that it might be sensible not to make match data a list, but a structure or structure of structures. Not 100% certain how to do that, but could be worth a shot. Each match would then be represented, something like follows:

`(struct match (win-name win-elo los-name los-elo))`

I don't know whether it would then make sense to have the match structures held in another structure, or to be put into a list of structures. 



## 2020-04-22 

I didn't have a great deal of time to work on this project today. As my next major goal is to create a script that can batch process matches (i.e. reading in a CSV file of match results, and outputting a CSV of updated Elo ratings) I re-read and made notes on Racket ports, which seem like a tricky feature to me, and I've tried to understand them before. I see that they're flexible, and that by learning to handle them you're gaining exposure as to how to do any io in Racket, but it still seems like a steep hill to climb for CSV processing. I'm also not a hundred percent sure how this is done "functionally", and I worry that I'm trying to shoehorn Racket into how I would arrange a Python script.


I generated a small number of test players and Elo ratings (between 1200 and 750 to simulate a range of probabilities). Then I created a series of fake match results that pit these players against each other, more or less as if they had been Monrad paired in the first round (i.e. strongest seed playing second strongest, etc) — I deliberately introduced several upsets, especially at the lower end of the table. So I now have a reference file to test when reading into a Racket script. The next goal is simply to output the contents of the file in DrRacket, but I'll have to try that tomorrow. 


If I were really trying to test this, I would create a number that represented the "true" strength of each player, and use this to influence who won or lost a match, so that the Elo rating of the players would tend to reflect this underlying reality — that seems more complicated than this warrants at this stage. I don't want to prove Elo ratings work with this project (though that would be interesting to code and test), I just want to create a script or program that does the basic job. 


## 2020-04-21 

The Elo rating script does not work as I had envisaged; instead of specifying that the ratings should be input on the command line in the order "winner loser", you have to type the flag each time. This means typing more when entering commands, and I think it is unnecessary.  I suspect that this could be fixed by changing the program to use the "args" section of the command line function, which would then make the values available.


A second thing that I don't know how to do is specify that if one of the values entered for "winner" and "loser" is not entered, it should default to our baseline Elo for new players of 800. 


On fiddling about writing some more documentation about how it currently works, I notice that running the command `racket elo-rating-cli.rkt` without supplying additional arguments returns what I would expect for a match of 800 vs 800. 


Let's assume that the next milestone is to be able to read in a CSV of match results, which supplies the winner and loser ratings and the result of the match on each line. What this version of the script should return is a list of winner's and loser's ratings for each match, which corresponds to their original input position (so that no one will get confused). It might be better to be able to link a name or ID to each player so that the ratings can be followed clearly, but this may add a level of complexity I'm not ready to deal with yet.    


I also think that it might be a good idea to have the script echo back the ratings entered for each player, so that the change is visually represented and the user has the opportunity to notice they've made a typo or a mistake of some kind. 
