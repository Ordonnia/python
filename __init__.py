import requests
import json


class Users():
    def __init__(self, **kwargs):

        
        for name, value in kwargs.items():
            if name == "platform":
                self.platform = value
            if name == "query":
                self.query = value
        try:
            self.UserObject = requests.get(f"https://api.meaxisnetwork.net/v3/users/search?from={self.platform}&query={self.query}")
        except:
            raise ValueError("Missing 'platform' or 'query' keyword argument.")

        self.UserJSON = self.UserObject.json()
        for name, value in self.UserJSON.items():
            vars(self)[name] = value

        self.id = self.UserJSON["id"]

    def get_applications(self):
        ApplicationObject = requests.get(f"https://api.meaxisnetwork.net/v3/users/{self.id}/applications")

        ApplicationJSON = ApplicationObject.json()


        return ApplicationJSON

    def get_activity(self):

        ApplicationObject = requests.get(f"https://api.meaxisnetwork.net/v3/users/{self.id}/activity")

        ApplicationJSON = ApplicationObject.json()


        return ApplicationJSON

    def get_creations(self):

        ApplicationObject = requests.get(f"https://api.meaxisnetwork.net/v3/users/{self.id}/creations")

        ApplicationJSON = ApplicationObject.json()


        return ApplicationJSON

class Funfact():
    def __init__(self):
        self.FunfactObject = requests.get("https://api.meaxisnetwork.net/v2/funfact")
        FunfactJSON = self.FunfactObject.json()
        self.author = FunfactJSON["author"]
        self.id = FunfactJSON["id"]
        self.funfact = FunfactJSON["text"]

class LeafyStatus():
    def __init__(self):
        self.LeafyStatus = requests.get("https://api.meaxisnetwork.net/v2/leafy")
        self.status_code = self.LeafyStatus.status_code

        if self.status_code == 200:
            self.status_result = "Online"
        else:
            self.status_result = "Offline"

class Account():
    def __init__(self, **kwargs):

        self.sesscook = ""
        
        for name, value in kwargs.items():
            if name == "sesscook":
                self.sesscook = value
            if name == "logcook":
                self.logcook = value

        cookies = {"sesscook": self.sesscook, "logcook": self.logcook}
        self.AccountObject = requests.get("https://api.meaxisnetwork.net/v3/accounts", cookies=cookies)
        self.AccountJSON = self.AccountObject.json()
        for name, value in self.AccountJSON.items():
            vars(self)[name] = value

    def get_all(self):
        return vars(self)

    def update(self, **kwargs):
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

class Shop():
    def __init__(self):
        GetAllShopItemRequest = requests.get("https://api.meaxisnetwork.net/v3/shop")
        self.items = GetAllShopItemRequest.json()

    def get_by_id(self, cls, **kwargs):

        id = None

        for name, value in kwargs.items():
            if name == "id" or name == "creationid" or name == "shopid":
                id = value

        GetItemRequest = requests.get(f"https://api.meaxisnetwork.net/v3/shop/{id}")
        return GetItemRequest.json()

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
            if name == "id" or name == "creationid":
                CreationID = value
            if name == "name":
                UpdateDict["name"] = value
            if name == "description":
                UpdateDict["description"] = value
            if name == "profilepicture" or name == "image":
                UpdateDict["pfp"] = value

        cookies = {"logcook": self.logcook, "sesscook": self.sesscook}
        PatchRequest = requests.patch(f"https://api.meaxisnetwork.net/v3/creations/{CreationID}/update", cookies=cookies, data=UpdateDict)

        GetRequest = requests.get(f"https://api.meaxisnetwork.net/v3/creations/{CreationID}", cookies=cookies)
        
        for name, value in GetRequest.json().items():
            vars(self)[name] = value




