import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	# Convert the dictionary to a JSON string
	json_string = json.dumps(data)

	# Upload the JSON string to IPFS
	cid = ipfs.add(json_string)

	return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	# Use the CID to access the JSON string on IPFS
	content = ipfs.cat(cid)

	# Convert JSON string to a Python dictionary
	data = jason.loads(content)

	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data
