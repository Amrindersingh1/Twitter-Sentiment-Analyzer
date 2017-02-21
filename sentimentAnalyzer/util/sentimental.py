from textblob import TextBlob
from sentimentAnalyzer.util.FetchTweets import FetchData
import re


class Analyzer():
    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def analyzeData(self, tag):

        fetcher = FetchData()
        public_tweets = fetcher.getTwitterData(tag)

        final_list = []
        pos = 0
        neg = 0
        net = 0
        pie_data = []

        if len(public_tweets) > 0:
            for tweet in public_tweets:
                tweet_dict = {}

                analysis = TextBlob(self.clean_tweet(tweet.text))

                pol = float("{0:.2f}".format(analysis.sentiment.polarity))

                if pol < 0:
                    neg += 1
                elif pol > 0:
                    pos += 1
                else:
                    net += 1

                tweet_dict['tweet'] = tweet.text
                tweet_dict['user'] = tweet.user.screen_name
                tweet_dict['polarity'] = pol

                final_list.append(tweet_dict)

        total = pos + neg + net
        if total == 0:
            net = 1
            total = 1

        pos = float("{0:.2f}".format((pos / total) * 100))
        neg = float("{0:.2f}".format((neg / total) * 100))
        net = float("{0:.2f}".format((net / total) * 100))

        pie_data.append(net)
        pie_data.append(pos)
        pie_data.append(neg)

        return {'tweet_list': final_list, 'pie_list': pie_data, 'count': total}
