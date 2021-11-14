#Scape from Stockscores

import requests
from bs4 import BeautifulSoup

def get_score(ticker):
	print("hi")
	try:
		url = f"https://www.stockscores.com/charts/charts/?ticker={ticker}"
		soup = BeautifulSoup(requests.get(url).content, "html.parser")

		score = soup.select(".nobottommargin+ .nobottommargin b")[1].text
		return int(score)
	except:
		raise ValueError