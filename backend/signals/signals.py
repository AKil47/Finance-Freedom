#Stock Scores
from . import stockscores
from . import esg_enterprise
from . import wsb_sentiment

signals = ["Sentiment S-Score", "ESG Enterprise", "WSB Sentiment"]

def is_stock_valid(stock):
	#TODO: Return if stock ticker is valid
	return True

def get_score(stock, signals_input):
	if not is_stock_valid(stock):
		return None

	ret = {
		"stock_id": stock
	}

	if "Sentiment S-Score" in signals_input:
		#Sentiment Stockstore 0 - 100
		ret["stockscore"] = stockscores.get_score(stock)

	if "ESG Enterprise" in signals_input:
		#Dividing by 10 to normalize score from 0 - 1000 to 0 - 100
		ret["ESG Enterprise"] = esg_enterprise.get_score(stock) / 10

	if "WSB Sentiment" in signals_input:
		#Range from -1 to 1. We need to normalize to 0 - 100
		ret["WSB Sentiment"] = wsb_sentiment.get_score(stock)

	return ret