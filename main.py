from dotenv import load_dotenv
import requests
import bs4 as bs
import os
import openai

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

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

print(tweet["choices"][0]["text"].strip())


