# Annotate tweets

A simple python script which takes a file which has a list of tweet ids and allows you to create the same file but wiht an additional attribute specifying if the tweet is "not relevant/relevant/informative".

Since Twitter only allows 100 tweets per request, you have to specify the start index from which you want to start parsing your original file after every 100 id. This script will also drop any unavailable id.

Inputs: File name and start index (0,100, 200...etc)