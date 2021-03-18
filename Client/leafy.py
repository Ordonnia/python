import requests

class LeafyStatus():
	def __init__(self):

		'''
		Gets the status of the leafy API.
		'''


		self.LeafyStatus = requests.get("https://api.meaxisnetwork.net/v2/leafy")
		self.status_code = self.LeafyStatus.status_code

		if self.status_code == 200:
			self.status_result = "Online"
		else:
			self.status_result = "Offline"