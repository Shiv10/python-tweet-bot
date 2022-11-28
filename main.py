import requests
import bs4 as bs

resp = requests.get('http://www.jimprice.com/generator/generate.php')
soup = bs.BeautifulSoup(resp.text, features='lxml')

b = soup.find('b')
term = ' '.join(b.text.strip().split())
print(term)