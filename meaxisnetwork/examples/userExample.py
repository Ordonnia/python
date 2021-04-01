from meaxisnetwork import users

Meaxis = users.User(platform = "username", query = "Meaxis")

# JSON of the User Object

print(Meaxis.UserJSON)


# Any attribute of the user object will be a variable to use.

print(Meaxis.username + Meaxis.id + Meaxis.description)

