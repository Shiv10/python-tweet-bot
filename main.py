import bs4 as bs
from datetime import datetime
from dotenv import load_dotenv
import openai
import os
import pytz
import requests
import time
import tweepy

load_dotenv()

def api():
    auth = tweepy.OAuthHandler(os.getenv('TWITTER_API_KEY'), os.getenv('TWITTER_API_SECRET'))
    auth.set_access_token(os.getenv('TWITTER_ACCESS_TOKEN'), os.getenv('TWITTER_ACCESS_TOKEN_SECRET'))

    return tweepy.API(auth)

def post_tweet(api: tweepy.API, message: str):
    api.update_status(message)
    date = datetime.now(pytz.timezone('Asia/Kolkata'))
    print('\nTweeted:\n{}\nat : {}'.format(message, date))


openai.api_key = os.getenv('OPENAI_API_KEY')
twitterApi = api()

for i in range(45):
    resp = requests.get('http://www.jimprice.com/generator/generate.php')
    soup = bs.BeautifulSoup(resp.text, features='lxml')

    b = soup.find('b')
    term = ' '.join(b.text.strip().split())

    tweet = openai.Completion.create(
        model='text-davinci-002',
        prompt='Write a funny tweet by Elon Musk on the topic "' + str(term)+ '"',
        max_tokens=350,
        temperature=0.95
    )

    tweet = tweet["choices"][0]["text"].strip()
    post_tweet(twitterApi, tweet)
    print('\nGoing to sleep...see you tomorrow')
    time.sleep(60*60*24)
    print('Time to wake up. Time right now is: {}'.format(datetime.now(pytz.timezone('Asia/Kolkata'))))
