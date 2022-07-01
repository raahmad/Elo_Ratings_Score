# Elo_Ratings_Score

### Intro
Aimed to observe which NBA games have more significance historically, compared NBA games from 1946-2018 using ELO ratings, and graphed the pre and post ELO rating of Lebron James’ final game in Cleveland to date: 6/8/2018



### ELO Rating is made up of 3 components:
1. The final score of each game
2. Where the game was played
3. When the game was played

### ELO ratings are zero sum:
A team gets the same amount of ELO rating points for a win as the team they beat gets docked for the loss.

### Usefulness
They are useful as a consistent statistic over the entire history of the league and it factors in things like relative strength of the league at the time.

### What is a good ELO rating?
1. An ELO rating of 1800 and above would make that team considered an all time great
    Usually a 67+ win team over an 82 game schedule
    2017 Golden State Warriors have the highest ELO rating in the history of the NBA with 1846
2. An ELO rating around 1700 would make that team considered a title contender
    Usually a 60-67 win team over an 82 game schedule
3. An ELO rating around 1600 would make that team considered a playoff team
    Usually a 51-60 win team over an 82 game schedule
4. An ELO rating around 1500 would be considered average
    Usually a 41-51  win team over an 82 game schedule
5. An ELO rating around 1400 would make that team considered a lottery team
    Usually a 31-41 win team over an 82 game schedule
6. An ELO rating below 1400 means that team is very bad
    Usually a 30 win and below team over an 82 game schedule


### Code Implementation
Three packages used
1. CSV
2. Matplotlib
3. Numpy

Broke up code into two files: main.py and utilities.py
1. Main contains all the code for the GUI
2. Utilities contains only the code for the graph

Data source:https://github.com/jtcies/nba-elo/blob/master/data/nba_elo_538.csv







