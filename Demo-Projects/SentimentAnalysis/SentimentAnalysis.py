import tweepy
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import unicodedata
import yaml
import csv
import sys

'''http://tech.thejoestory.com/2015/01/python-textblob-sentiment-analysis.html
'''

def get_api_accessor():  
    """
    gets an authenticated twitter api accessor object
    Returns:
        api: authenticated twitter api accessor object
    """
    conf = yaml.load(open('credentials.yml'))
    consumer_key= conf['user']['consumer_key'] 
    consumer_secret= conf['user']['consumer_secret']
    access_token=conf['user']['access_token']
    access_token_secret=conf['user']['access_token_secret']
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api


def show_recent_tweets(api,topicname):
    '''
    shows recent tweets on the given topic name
    Returns:
        public_tweets: list of all fetched tweets
    '''
    public_tweets = api.search(q=topicname)
    for tweet in public_tweets:
        print(tweet.text)
    return public_tweets


def perform_sentiment_analysis_and_make_csv(topicname,public_tweets):
    
    filename = topicname.replace(' ','_') +'_sentiment_dataset.csv'
    with open(filename, 'w',newline='\n') as f:
        fieldnames = ['Tweet','Polarity','Subjectivity','Classification',"P_pos","P_neg", ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        polarity="Neutralness"
        
        for tweet in public_tweets:
            analysisUsingPatternAnalyzer  = TextBlob(tweet.text)
            if(analysisUsingPatternAnalyzer.sentiment.polarity > 0):
                polarity = 'Positiveness'
            if(analysisUsingPatternAnalyzer.sentiment.polarity < 0):
                polarity = 'Negativeness'
                '''
                Textblob will train the analyzer before each run,Naive Bayes Classifier is slow
                we can use: https://stackoverflow.com/questions/33241842/textblob-naivebayesanalyzer-extremely-slow-compared-to-pattern
                example:
                from textblob import Blobber
                from textblob.sentiments import NaiveBayesAnalyzer
                tb = Blobber(analyzer=NaiveBayesAnalyzer())

                print tb("sentence you want to test")
                '''
            sentimentUsingNaiveBayesAnalyzer = TextBlob(tweet.text,analyzer=NaiveBayesAnalyzer()).sentiment


            try:
                writer.writerow({fieldnames[0]:tweet.text, fieldnames[1]:polarity, fieldnames[2]:analysisUsingPatternAnalyzer.sentiment.subjectivity,
                    fieldnames[3]:sentimentUsingNaiveBayesAnalyzer.classification,fieldnames[4]:sentimentUsingNaiveBayesAnalyzer.p_pos,fieldnames[5]:sentimentUsingNaiveBayesAnalyzer.p_neg})
            except UnicodeEncodeError as e:
                print(e)

print ('Logging in to twitter with your credentials ...')
try:
    api_accessor = get_api_accessor() 
    print ('Logged in!')
except tweepy.error.TweepError as e:
    print ('Couldnt Login, Check APIKEYS')
    sys.exit(1)
print('Enter the topic you want to collect the dataset on')
topic_name = input()
print('Showing recent tweets on the topic...')
public_recent_tweets = show_recent_tweets(api_accessor,topic_name)
print ('Writing it to {}_sentiment_dataset.csv'.format(topic_name))
perform_sentiment_analysis_and_make_csv(topic_name,public_recent_tweets)

print('Done.')



