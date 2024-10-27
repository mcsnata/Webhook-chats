# Chat via webhooks
# NATA VS EVERYBODY

# Modules
import requests # > pip install requests
import os
import time
from time import sleep
from datetime import datetime # > pip install datetime

time = datetime.now()
clock = time.strftime(' %H:%M %p')
os.system('title Webhook - Chat')

os.system('color d')
chats = input('Messages :')
message = {"content": '**Chat** : ' + chats + '\nAt Time : ' + clock}
print(f"[INFO] : Message sended")
response = requests.post("your webhook links", json=message)