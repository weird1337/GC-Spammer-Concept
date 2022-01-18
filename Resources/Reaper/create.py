###################################################
# .---. .----..----..-..-..---..---. 
# | |-< | || || || | \  / | |- | |-< 
# `-'`-'`----'`----'  `'  `---'`-'`-
###################################################
import httpx
import os
import time
from Resources import coloring
from dotenv import load_dotenv
###################################################
headers = {'authority': 'discord.com', 'accept': '*/*', 'accept-language': 'en-US,en;q=0.9', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36', 'x-discord-locale': 'en-GB', 'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk2LjAuNDY2NC4xMTAgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6Ijk2LjAuNDY2NC4xMTAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTA4OTI0LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=='}
class miners:
  def __init__(self):
    with open("Resources/Utils/Data/tokens.txt", "r") as f:
      workers = f.read().split('\n')
      self.workers = workers 

  def filter(self):
    valid = []
    for token in self.workers:
      if token != "\n":
        headers['authorization'] = token
        x = httpx.get("https://discord.com/api/v9/users/@me/library", headers=headers)
        if x.status_code == 200:
          valid.append(token)
      with open("Resources/Utils/Data/tokens.txt", "a+") as s:
        s.truncate(0)
        for a in valid:
          s.write(a + "\n")
  
class mine:
  def __init__(self, count):
    miners().filter()
    if os.stat("Resources/Utils/Data/tokens.txt").st_size == 0:
      print(f"{coloring.FAIL}\n  <───$:[No Valid Worker Tokens Provided]───>")
      return
    else:
      with open("Resources/Utils/Data/tokens.txt", "r") as valid:
        workers = valid.read().split("\n") # Gathers all valid tokens into a list of workers.
        self.workers = []
        for line in workers:
          if len(line) != 0:
            self.workers.append(line)
      self.count = round(int(count) / len(self.workers))
      load_dotenv()
      self.id = os.getenv('ID')
    
  def work(self):
      first = True
      for i in range(self.count):
        if i%10 == 0 and first == False:
          time.sleep(300)
        else:
          first = False
          for worker in self.workers:
                headers['authorization'] = worker
                group = httpx.post("https://discord.com/api/v9/users/@me/channels", headers=headers, json={'recipients': []})
                if group.status_code == 200:
                  print(f"{coloring.GREEN}\n  <───$:[Created Group Chat]───>")
                  httpx.put(f"https://discord.com/api/v9/channels/{group.json()['id']}/recipients/{self.id}", headers=headers)
                  with open("Resources/Utils/Data/gcs.txt", "a+") as f:
                    f.write(f"{group.json()['id']}\n")
                else:
                  print(f"{coloring.FAIL}\n  <───$:[Failed To Create Group Chat]───>")
###################################################