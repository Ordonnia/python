# MeaxisNetwork API Python Wrapper

## Introduction

This is a python wrapper to include MeaxisNetwork API Endpoints and requests into your code. The following endpoints are supported:

> Users  
> Accounts  
> Creations  
> Funfact  
> Shop  
> Vote

## Code Samples

### Get public user data from a MeaxisNetwork User

```python
from meaxisnetwork import users

Meaxis = users.User(platform = "username", query = "Meaxis")

# JSON of the User Object

print(Meaxis.UserJSON)


# Any attribute of the user object will be a variable to use.

print(Meaxis.username + Meaxis.id + Meaxis.description)

```

### Get all Shop Items in the MeaxisNetwork Shop
```python
from meaxisnetwork import shop

Shop = shop.Shop()
print(Shop.items)    
```    
                                                                                                        

## Installation

Go to the following link:  
```
https://pypi.org/project/meaxisnetwork
```

And then copy the installation link. 

### Windows

In the search bar, type in 'Command Prompt' and then press 'Yes' to the User Account Control Prompt.   

Then paste the command you copied and press enter.

### Linux

Run the following command in your terminal:
```
python3 -m pip install meaxisnetwork
```

If it says anything about python3 not being found, you need to install python with your Package Manger.

Debian:  

```
sudo apt-get install python
```
Arch:  
```
sudo pacman -S python
```
  
  
For other distributions, use your package manager to install python. 