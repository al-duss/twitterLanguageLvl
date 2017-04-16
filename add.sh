#!/bin/bash
cd MapReduce
hadoop jar wordcount.jar wordCount ./../DataGathering/tweets/$1_tweets.csv results/$1
