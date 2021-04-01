import os
import requests

if __name__ == "__main__":
    for f in os.listdir():
        if f.endswith(".py"):
            print(f"{f} was loaded.")

