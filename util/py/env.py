from dotenv import load_dotenv
import os

def loadEnv():
    load_dotenv()

    returner = {}

    for key in ["token", "serverid"]:
        getKey = os.getenv(key.upper())
        if getKey is None:
            log(f"Error: {key} not found in .env file.")
            exit(1)
        else:
            returner[key.upper()] = getKey
    
    return returner
