import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	# Convert the dictionary to a JSON string
	files = json.dumps(data)

	# Upload the JSON string to IPFS
	response = requests.post('https://ipfs.infura.io:5001/api/v0/add', files=files)
	print(response.text)
	return response

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	# Use the CID to access the JSON string on IPFS
	ipfs = ipfs.Client()
	content = ipfs.cat(cid)

	# Convert JSON string to a Python dictionary
	data = jason.loads(content)

	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data
