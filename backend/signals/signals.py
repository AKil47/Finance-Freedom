#Stock Scores
from . import stockscores
from . import esg_enterprise
from . import wsb_sentiment

signals = ["Sentiment S-Score", "ESG Enterprise", "WSB Sentiment"]

def maprange(a, b, s):
	'''Maps one range onto another range'''
	(a1, a2), (b1, b2) = a, b
	return  b1 + ((s - a1) * (b2 - b1) / (a2 - a1))

def is_stock_valid(stock):
	#TODO: Return if stock ticker is valid
	return True

def get_score(stock, signals_input):
	if not is_stock_valid(stock):
		return None

	ret = dict()

	if "Sentiment S-Score" in signals_input:
		#Sentiment Stockstore 0 - 100
		ret["stockscore"] = stockscores.get_score(stock)

	if "ESG Enterprise" in signals_input:
		#Dividing by 10 to normalize score from 0 - 1000 to 0 - 100
		score = esg_enterprise.get_score(stock)
		ret["ESG Enterprise"] = maprange((0, 1000), (0, 100), score)

	if "WSB Sentiment" in signals_input:
		#Range from -1 to 1. We need to normalize to 0 - 100
		score = wsb_sentiment.get_score(stock)
		ret["WSB Sentiment"] = maprange((-1, 1), (0, 100), score)

	return {
		"stock_id": stock,
		"signals": ret
	}