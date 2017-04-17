# Twitter Language Level

### Dependencies

This project is written in Java and Python 2.7, and can be ran using the bash scripts.
For Python, it uses the tweepy API from twitter to get user tweets, and the matplotlib pyplot library for visualization purposes.
For Java, it uses Hadoop to parse through the tweets.

### Running The Program

The shell scripts can be used to run the program.
The file list.txt contains the twitter usernames that will be analyzed, and they are currently seperated by category (musician, politician, education, etc.)  
List.sh will find the 2000 latest tweets of every user listed in list.txt, then mapreduce the tweets to find the number of words used throughout, as well as how many different ones have been used.  
Add.sh _username_ will find the tweets and mapreduce them as did list.sh, but on an individual basis. However, using this will not let it be used for the visualization.  
show.sh _category_ will show the graph with the vocabulary level and verbosity of the users, with category being one of ['Musicians', 'Politicians', 'Athletes', 'News Stations', 'Businesses', 'Education', 'Entertainers], and if left blank will show that graph will all of them.
