import requests
import json
from .utils import check_response, HTTPRequest

class Creations():
	def __init__(self, **kwargs):

		self.logcook = None
		self.sesscook = None

		for name, value in kwargs.items():
			if name == "logcook":
				self.logcook = value
			if name == "sesscook":
				self.sesscook = value

		from .credentials import Credentials
		try:
			if Credentials.credentials != None and Credentials.credentials["logcook"] is not None:
				if self.logcook != None and self.sesscook != None:
					return
				Credentials = Credentials.credentials
				self.logcook = Credentials["logcook"]
				self.sesscook = Credentials["sesscook"]
		except:
			pass

		CreationRequest = HTTPRequest('creations', 'get', cookies = {"logcook": self.logcook, "sesscook": self.sesscook})

		self.CreationList = CreationRequest.json()

	def get_by_id(self, **kwargs):
		for name, value in kwargs.items():
			if name == "logcook":
				self.logcook = value
			if name == "sesscook":
				self.sesscook = value
			if name == "id" or "creationid":
				self.creationid = value

		CreationRequest = HTTPRequest(f"creations/{self.creationid}", 'get', cookies = {"logcook": self.logcook, "sesscook": self.sesscook})
		return CreationRequest.json()

	def create(self, **kwargs):

		CreationName = None
		description = None

		for name, value in kwargs.items():
			if name == "name":
				CreationName = value
			if name == "description" or name == "desc":
				description = value

		PostRequest = HTTPRequest('creations/new', 'post', cookies = {"logcook": self.logcook, "sesscook": self.sesscook}, data = {"name": CreationName, "description": description})
		return PostRequest.json()

	def update(self, **kwargs):

		UpdateDict = {}
		CreationID = None

		for name, value in kwargs.items():
			vars(self)[key] = value

		cookies = {"logcook": self.logcook, "sesscook": self.sesscook}
		PatchRequest = HTTPRequest(f'creations/{CreationID}/update', 'patch', cookies=cookies, data=UpdateDict)

		GetRequest = HTTPRequest(f"creations/{CreationID}", 'get', cookies=cookies)
		
		for name, value in GetRequest.json().items():
			vars(self)[name] = value