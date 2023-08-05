from util.py.helper import log, bashCommand

url = "https://google.com"

print(bashCommand(f"curl https://monitor-api.vercel.app/api/public?url={url} -s"))
