import requests
import json
from .utils import check_response

class Creations():
	def __init__(self, **kwargs):
		for name, value in kwargs.items():
			if name == "logcook":
				self.logcook = value
			if name == "sesscook":
				self.sesscook = value

		CreationRequest = requests.get("https://api.meaxisnetwork.net/v3/creations", cookies = {"logcook": self.logcook, "sesscook": self.sesscook})

		self.CreationList = CreationRequest.json()

	def get_by_id(self, **kwargs):
		for name, value in kwargs.items():
			if name == "logcook":
				self.logcook = value
			if name == "sesscook":
				self.sesscook = value
			if name == "id" or "creationid":
				self.creationid = value

		CreationRequest = requests.get(f"https://api.meaxisnetwork.net/v3/creations/{self.creationid}", cookies = {"logcook": self.logcook, "sesscook": self.sesscook})
		return CreationRequest.json()

	def create(self, **kwargs):

		CreationName = None
		description = None

		for name, value in kwargs.items():
			if name == "name":
				CreationName = value
			if name == "description" or name == "desc":
				description = value

		PostRequest = requests.post(f"https://api.meaxisnetwork.net/v3/creations/new?name={CreationName}&description={description}", cookies = {"logcook": self.logcook, "sesscook": self.sesscook})
		return PostRequest.json()

	def update(self, **kwargs):

		UpdateDict = {}
		CreationID = None

		for name, value in kwargs.items():
			vars(self)[key] = value

		cookies = {"logcook": self.logcook, "sesscook": self.sesscook}
		PatchRequest = requests.patch(f"https://api.meaxisnetwork.net/v3/creations/{CreationID}/update", cookies=cookies, data=UpdateDict)

		GetRequest = requests.get(f"https://api.meaxisnetwork.net/v3/creations/{CreationID}", cookies=cookies)
		
		for name, value in GetRequest.json().items():
			vars(self)[name] = value