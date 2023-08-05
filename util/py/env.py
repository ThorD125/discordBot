from dotenv import load_dotenv
import os

def loadEnv():
    load_dotenv()

    token = os.getenv('TOKEN')
    if token is None:
        log("Error: Bot token not found in .env file.")
        exit(1)

    serverid = os.getenv('SERVERID')
    if serverid is None:
        log("Error: Server ID not found in .env file.")
        exit(1)
    
    return {"TOKEN": token, "SERVERID": serverid}
