import tweepy
import json

# Authenticate to Twitter
auth = tweepy.OAuthHandler("E5V3z0hWwAZiCgyQxQ9yqodeD", "nem5pG7773EJ59XaZSD9EzXvVJrNuxNNXnbQu2tkgBFOft44HB")
auth.set_access_token("1304990944316461058-uSNbZKYsQYt4SMtztBcpK6m8qRhGrn", "cvu6nn1sMmFNMZrgj3p47lF6pm19dnKv4izxiWym2kdvT")

# Create API object
api = tweepy.API(auth)
try:
    api.verify_credentials()
    print("Successfully Authenticated")
    print("Initializing API...")
    print("Tweepy version", tweepy.__version__)
except:
    print("Error during authentication")

"""
public_tweets = api.home_timeline()
"""
"""
for tweet in public_tweets:
    print(tweet.text)
    print()
"""
"""
status = public_tweets[0]

#convert to string
json_str = json.dumps(status._json)

#deserialise string into python object
parsed = json.loads(json_str)

#print(json.dumps(parsed, indent=4, sort_keys=True))
print(status.text)
"""

"""



userID = "realDonaldTrump"

all_tweets.extend(tweets)
oldest_id = tweets[-1].id
while True:
    tweets = api.user_timeline(screen_name=userID, 
                           # 200 is the maximum allowed count
                           count=200,
                           include_rts = False,
                           max_id = oldest_id - 1,
                           # Necessary to keep full_text 
                           # otherwise only the first 140 words are extracted
                           tweet_mode = 'extended'
                           )
    if len(tweets) == 0:
        break
    oldest_id = tweets[-1].id
    all_tweets.extend(tweets)
    print('N of tweets downloaded till now {}'.format(len(all_tweets)))
for info in tweets[:3]:
     print("ID: {}".format(info.id))
     print(info.created_at)
     print(info.full_text)
     print("\n")
"""




screen_name = "realDonaldTrump"
alltweets = []  

#make initial request for most recent tweets (200 is the maximum allowed count)
new_tweets = api.user_timeline(screen_name = screen_name,count=200)

#save most recent tweets
alltweets.extend(new_tweets)

#save the id of the oldest tweet less one
oldest = alltweets[-1].id - 1

#keep grabbing tweets until there are no tweets left to grab
while len(new_tweets) > 0:
    print(f"getting tweets before {oldest}")
    
    #all subsiquent requests use the max_id param to prevent duplicates
    new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
    
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #update the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    print(f"...{len(alltweets)} tweets downloaded so far")

#transform the tweepy tweets into a 2D array that will populate the csv 
outtweets = [[tweet.id_str, tweet.created_at, tweet.text] for tweet in alltweets]

