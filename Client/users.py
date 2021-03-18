import requests
import json
from .utils import check_response


class User():


	def __init__(self, **kwargs):

		'''
		The Users class that gives you public information about the user by the parameters you give it:

		Examples:

		Users(platform = username, query = "Meaxis")
		'''


		for name, value in kwargs.items():
			if name == "platform":
				self.platform = value
			if name == "query":
				self.query = value
		try:
			self.UserObject = requests.get(f"https://api.meaxisnetwork.net/v3/users/search?from={self.platform}&query={self.query}")
		except:
			raise ValueError("Missing 'platform' or 'query' keyword argument.")

		try:
			self.UserJSON = self.UserObject.json()
			for name, value in self.UserJSON.items():
				vars(self)[name] = value
		except:
			ErrorResponse = check_response(self.UserObject)
			raise ValueError(ErrorResponse)

	def get_applications(self):
		'''

		Gets all of the applications of the user that you have given it. Takes no parameters.
		
		'''
		ApplicationObject = requests.get(f"https://api.meaxisnetwork.net/v3/users/{self.id}/applications")

		ApplicationJSON = ApplicationObject.json()


		return ApplicationJSON

	def get_activity(self):
		
		'''
		
		Gets all of the feeds the user has sent through the MeaxisNetwork

		'''


		ApplicationObject = requests.get(f"https://api.meaxisnetwork.net/v3/users/{self.id}/activity")

		ApplicationJSON = ApplicationObject.json()


		return ApplicationJSON

	def get_creations(self):

		'''
		
		Gets all of the creations the user has on the MeaxisNetwork.

		'''

		ApplicationObject = requests.get(f"https://api.meaxisnetwork.net/v3/users/{self.id}/creations")

		ApplicationJSON = ApplicationObject.json()


		return ApplicationJSON