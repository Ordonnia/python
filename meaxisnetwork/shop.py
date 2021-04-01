import json
import requests
from .utils import check_response, HTTPRequest

class Shop():
	def __init__(self):
		GetAllShopItemRequest = HTTPRequest("shop", 'get')
		try:
			self.items = GetAllShopItemRequest.json()
		except:
			ErrorResponse = check_response(GetAllShopItemRequest)
			raise ValueError(ErrorResponse)

	def get_by_id(self, cls, **kwargs):

		id = None

		for name, value in kwargs.items():
			if name == "id" or name == "creationid" or name == "shopid":
				id = value

		GetItemRequest = HTTPRequest(f"shop/{id}", 'get')
		if check_response(GetItemRequest):
			return GetItemRequest.json()