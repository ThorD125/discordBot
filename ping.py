import os


ip = "127.0.0.1"


response = os.popen(f"ping -c 4 {ip} ").read()
print(response)
