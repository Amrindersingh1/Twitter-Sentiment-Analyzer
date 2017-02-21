import tweepy

consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""


class FetchData():

    def getTwitterData(self, tag):
        try:
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)

            api = tweepy.API(auth)

            public_tweets = api.search( q = tag, count=100,language = 'en' )

            return public_tweets

        except tweepy.TweepError as e:
            print("Error : " + str(e))


