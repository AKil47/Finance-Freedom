#Stock Scores
from . import stockscores
from . import esg_enterprise
from . import wsb_sentiment
from . import twitter_general
from . import twitter_specific

signals = ["Sentiment S-Score", "ESG Enterprise", "WSB Sentiment", "Twitter General", "Twitter Specific"]

def maprange(a, b, s):
	'''Maps one range onto another range'''
	(a1, a2), (b1, b2) = a, b
	return  b1 + ((s - a1) * (b2 - b1) / (a2 - a1))

def is_stock_valid(stock):
	#TODO: Return if stock ticker is valid
	return True

def get_score(stock, signals_input):
	signals_dict = dict()
	for signal in signals_input:
		signals_dict[signal.signal] = signal.weight

	#Weighted score calc
	weight_total = sum(signals_dict.values())
	scale_factor = 100 / weight_total

	if not is_stock_valid(stock):
		return None

	ret = dict()

	total = 0

	if "Sentiment S-Score" in signals_dict:
		#Sentiment Stockstore 0 - 100
		ret["Sentiment S-Score"] = stockscores.get_score(stock)

		weight = scale_factor * signals_dict["Sentiment S-Score"] / 100
		total += weight * ret["Sentiment S-Score"]

	if "ESG Enterprise" in signals_dict:
		#Dividing by 10 to normalize score from 0 - 1000 to 0 - 100
		score = esg_enterprise.get_score(stock)
		ret["ESG Enterprise"] = maprange((0, 1000), (0, 100), score)

		weight = scale_factor * signals_dict["ESG Enterprise"] / 100
		total += weight * ret["ESG Enterprise"]

	if "WSB Sentiment" in signals_dict:
		#Range from -1 to 1. We need to normalize to 0 - 100
		score = wsb_sentiment.get_score(stock)
		ret["WSB Sentiment"] = maprange((-1, 1), (0, 100), score)

		weight = scale_factor * signals_dict["WSB Sentiment"] / 100
		total += weight * ret["WSB Sentiment"]

	if "Twitter General" in signals_dict:
		score = twitter_general.get_score(stock)
		#Range from -1 to 1. We need to normalize 0 - 100
		ret["Twitter General"] = maprange((-1, 1), (0, 100), score)

		weight = scale_factor * signals_dict["Twitter General"] / 100
		total += weight * ret["Twitter General"]

	if "Twitter Specific" in signals_dict:
		if stock = "TSLA":
			stock = "Tesla"
		score = twitter_general.get_score("elonmusk", stock)
		#Range from -1 to 1. We need to normalize 0 - 100
		ret["Twitter Specific"] = maprange((-1, 1), (0, 100), score)

		weight = scale_factor * signals_dict["Twitter Specific"] / 100
		total += weight * ret["Twitter Specific"]	


	return {
		"stock_id": stock,
		"signals": ret,
		"total": total
	}