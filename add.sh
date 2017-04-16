#!/bin/bash
python ./DataGathering/twitter.py $1 
cd MapReduce
hadoop jar wordcount.jar wordCount ./../DataGathering/tweets/$1_tweets.csv results/$1
