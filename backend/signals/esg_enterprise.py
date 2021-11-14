#ESG Enterprise Query

import requests
import json

url = "https://tf689y3hbj.execute-api.us-east-1.amazonaws.com/prod/authorization/search"

def get_score(ticker):

	#It's a bad idea to expose my token but I don't really care
	querystring = {"q":ticker,"token":"db5e5aabfd3c96f418c9d5914b2eaab5","":""}

	payload = ""
	response = requests.request("GET", url, data=payload, params=querystring).content

	response = json.loads(response)

	ret = response[0]["total"]

	return ret