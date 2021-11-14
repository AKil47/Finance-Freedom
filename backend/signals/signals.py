#Stock Scores
from . import stockscores

signals = ["Sentiment S-Score"]

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

	return ret