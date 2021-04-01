import requests
import json
from .utils import check_response

class VoteType():


	def __init__(self):
		pass

	@classmethod
	def Up(cls):
		return {"object": "Vote.VoteType", "votetype": "Up"}

	@classmethod
	def Unvote(cls):
		return {"object": "Vote.VoteType", "votetype": "Up"}

	@classmethod
	def Down(cls):
		return {"object": "Vote.VoteType", "votetype": "Down"}


class Vote():
	def __init__(self, **kwargs):
		for key, value in kwargs.items():
			if key.lower() != "votetype":
				vars(self)[key.lower()] = value
			else:
				if type(VoteType):
					vars(self)[key.lower()] = value["votetype"]
				else:
					raise ValueError("Key 'votetype' is not type Vote.VoteType")

		Patch = HTTPRequest(f"vote/{self.id}", 'patch', data = {"vote": self.votetype}, cookies = {"logcook": self.logcook, "sesscook": self.sesscook})
		for key, value in Patch.json().items():
			vars(self)[key] = value