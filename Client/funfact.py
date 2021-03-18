import requests
import json
from .utils import check_response

class Funfact():
	def __init__(self):

		'''

		Gets a random funfact from the API.

		'''


		self.FunfactObject = requests.get("https://api.meaxisnetwork.net/v2/funfact")
		try:
			FunfactJSON = self.FunfactObject.json()
			self.author = FunfactJSON["author"]
			self.id = FunfactJSON["id"]
			self.funfact = FunfactJSON["text"]
		except:
			ErrorResponse = check_response(self.FunfactObject)
			raise ValueError(ErrorResponse)