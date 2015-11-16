# Lab 6
## Participants: Denis Khryashchev (dk2926)

## Data: MTA_Fare.npy that can be accessed from:
http://cosmo.nyu.edu/~fb55/UI_CUSP_2015/data/

## Notebook: subway_timeseries-dk2926.ipynb

## Assignment 1: Event detection: Identify the most prominent event. There is a very significant drop (>3-sigma) in all time series.
Identify it and figure out what it is due to.

## Answer to the questions in task 1: The only event in the data that is outside of 3 sigmas is ['2012-10-20T20:00:00.000000000-0400'], the event that happened on October, 20, 2012 at 8 p.m. The event is Hurricane Sandy.


## Assignment 2: Some of the time series are stationary, some have a complex structure, some show a downward trend: Identify the ridership types that have steadily increased in popularity, and that have steadily decreased. by how much? (e.g what is the ratio of usage in the first 10 and last 10 weeks)

## Answer to the questions in task 2: Based on the flux ratios, 'mr' and 'spec' have the strongest increase in popularity trend by 145,474 and 32,813 correspondingly. The others are 'sen' (60,524), 'rr' (105,601), '7d' (1,649,944), '14d' (144,336).

'ez', 'exp', 'afas' have the strongest decrease in popularity trend, that is almost approaching 0 with the absolute decrease by 593,382; 323,400 and 11,024 correspondingly.


## Assignment 3: Several stations show a prominent annual periodicity. Identify the 4 stations (indentify them by the index of their location in the data cube) that show the most prominent periodic trend on an annual period (52 weeks). (Can you figure out what the periodic peak in rides is due to?)

## Answer to the questions in task 3: Having the indeces starting at 0, 4 stations that show the prominent annual periodicity trend are 1, 195, 151 and 328.