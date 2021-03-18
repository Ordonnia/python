import requests
import json
from .utils import check_response

class Account():
	def __init__(self, **kwargs):

		'''
		An Account Object is an object with all of the information of a user (incl. private info)

		Requires a sesscook and logcook.
		'''
		
		for name, value in kwargs.items():
			if name == "sesscook":
				self.sesscook = value
			if name == "logcook":
				self.logcook = value

		from .credentials import Credentials
		try:
			if Credentials.credentials != None and Credentials.credentials["logcook"] is not None:
				Credentials = Credentials.credentials
				self.logcook = Credentials["logcook"]
				self.sesscook = Credentials["sesscook"]
		except:
			pass
		cookies = {"sesscook": self.sesscook, "logcook": self.logcook}
		self.AccountObject = requests.get("https://api.meaxisnetwork.net/v3/accounts", cookies=cookies)
		if self.AccountObject.status_code == 200:
			self.AccountJSON = self.AccountObject.json()
			for name, value in self.AccountJSON.items():
				vars(self)[name] = value
		else:
			response_text = self.AccountObject.text
			error_code = response_text[-9:].replace("(", "").replace(")", "")
			self.error_data = {"error_message": response_text.replace(error_code, ""), "http-status-code": self.UserObject.status_code, "documentation_reference": f"https://meaxisnetwork.net/create/docs/api/error-codes#{error_code}"}
			for name, value in self.error_data.items():
				vars(self)[name] = value
	def get_all(self):

		'''
		Deprecated Instance Method that returns all vars
		'''


		return vars(self).items()

	def update(self, **kwargs):

		'''
		Updates the description, email, contact or location of the account you are connected to.
		'''


		UpdateDict = {}

		for name, value in kwargs.items():

			if name == "email":
				UpdateDict["email"] = value
			if name == "contact":
			   UpdateDict["contact"] = value
			if name == "location":
				UpdateDict["location"] = value
			if name == "description":
				UpdateDict["description"] = value

		cookies = {"sesscook": self.sesscook, "logcook": self.logcook}
		requests.patch("https://api.meaxisnetwork.net/v3/accounts/update", cookies=cookies, data=UpdateDict)

		RefreshRequest = requests.get("https://api.meaxisnetwork.net/v3/accounts/", cookies=cookies)

		for name, value in RefreshRequest.json().items():
			vars(self)[name] = value

		return RefreshRequest.json()


	def plugins(self, **kwargs):

		PluginName = None
		PluginState = None

		for name, value in kwargs:
			if name == "name":
				PluginName = value
			if name == "state":
				PluginState = value

		if PluginName == None or PluginState == None:
			raise ValueError("Required keyword arguments ['name', 'state'] are missing.")

		cookies = {"sesscook": self.sesscook, "logcook": self.logcook}
		requests.patch("https://api.meaxisnetwork.net/v3/accounts/plugins", cookies=cookies, data={"name": PluginName, "state": PluginState})
