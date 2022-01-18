#ESG Enterprise Query

import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("ESG_TOKEN")

url = "https://tf689y3hbj.execute-api.us-east-1.amazonaws.com/prod/authorization/search"

def get_score(ticker):

	querystring = {"q":ticker,"token":token,"":""}

	payload = ""
	response = requests.request("GET", url, data=payload, params=querystring).content

	response = json.loads(response)

	ret = response[0]["total"]

	return ret