import requests
import json


def showPNRStatus():
	pnr = int(input("Please enter your PNR:"))

	url = "https://indianrailways.p.rapidapi.com/index.php"

	querystring = {"pnr": pnr}

	headers = {
	    'x-rapidapi-host': "indianrailways.p.rapidapi.com",
	    'x-rapidapi-key': "bf6c102084mshed82bef1ade50d5p196f8djsn99c18233c60f"
	    }

	response = requests.request("GET", url, headers=headers, params=querystring)

	responseJSON = response.json()

	if len(responseJSON['error']) > 0:
		print(responseJSON["error"])
	else:
		print("****************",responseJSON["chartingStatus"],"****************\n")
		print(responseJSON["journeyDetails"]["trainName"],"is ", responseJSON["journeyDetails"]["boardingDate"])


def showTrainRunningStatus():
	train_number = int(input("Please enter Train Number:")) 
	station_code = input("Please enter Station Code:")
	running_date = input("Please enter Date into dd-mm-yyyy format:")
	apikey = "9whzae6iew"
	
	train_api_endpoint = f"https://api.railwayapi.com/v2/live/train/{train_number}/station/{station_code}/date/{running_date}/apikey/{apikey}/"
	response = requests.get(url = train_api_endpoint, params = {})

	responseJSON = response.json()
	if responseJSON["response_code"] == 200:
		print(responseJSON["train"]["name"], " ", responseJSON["position"])
	else:
		print("Sorry there is no information of Train Number: ",  train_number)
	

	
showTrainRunningStatus()
showPNRStatus()



	
