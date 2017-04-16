#!/bin/bash
file="list.txt"
while IFS= read -r var
do
	python ./DataGathering/twitter.py "$var" 
	cd MapReduce
	hadoop jar wordcount.jar wordCount ./../DataGathering/tweets/"$var"_tweets.csv results/"$var"
	cd ..
done <"$file"
python ./Visualization/analyze.py