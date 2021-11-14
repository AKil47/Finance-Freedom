#WSB Sentiment (Reddit)

import pandas as pd

df = pd.read_csv("../backend/signals/historic_sentiment_analysis.csv")

def get_score(ticker):
	# ticker = "GOOGL"

	def normalize_date(date_input):
		ret = ""
		if "-" in date_input:
			date_input = date_input.split("-")
			ret = [date_input[1], date_input[2], date_input[0][-2:]]
			return "/".join(ret)
		else:
			return date_input

	df["date"] = df["date"].apply(normalize_date)

	latest = df[df["stock"] == ticker].iloc[-1]

	return latest["Total_Compound"]