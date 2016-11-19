'''
Handles all the requests to twitter.api
And Return a customized result
'''

import json
# Import the necessary methods from "twitter" library

from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Import the py file that contains all the variables for the twitter API's user credential

from api_keys import *

aouth = OAuth(Access_Token,Access_TokenSecret,Consumer_Key,Consumer_Secret)


# Initiate the connection to the twitter Streaming API

#twitter_stream = TwitterStream(auth=aouth)

# Initiate connection to userStream API

twitter_stream = TwitterStream(auth=aouth, domain='userstream.twitter.com')


#TODO make thos a function


# Get the a sample result of the public data following through twitter


#iterator = twitter_stream.statuses.sample()


# Get a custom search using filter

iterator = twitter_stream.statuses.filter(track="Trump", language="en")


# Print each tweet in the stream to the screen
# Here we set it to stop after getting 10 tweets.
# You don't have to set it to stop, but can continue running
# the Twitter API to collect data for days or even longer.

#TODO END



#TODO make this a object
tweet_count = 4
for tweet in iterator:
    tweet_count -= 1
    # Twitter Python Tool wraps the data returned by Twitter
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    # The command below will do pretty printing for JSON data, try it out

    #tweet_file = open("tweet.txt", 'w')
    #json.dump(tweet,tweet_file, indent=4)     #Saves or stores the json result into a text file for a later usage


    json_tweet = json.dumps(tweet, indent=4)   # Parse the request result in json and Save in a variable

    # Make the json variale available for us to pull values
    # It's really important otherwise you won't get no result

    tweets = json.loads(json_tweet)
    if 'text' in tweets:
        print(tweets['text'])
        print(tweets['user']['name'])
        print(tweets['user']['screen_name'] +'\n\n')



    if tweet_count <= 0:
        # with open("tweet.txt", 'r') as f:
        #     read_file = f.read()
        #     print(read_file)
        #tweet_file.close()
        break

#TODO END




