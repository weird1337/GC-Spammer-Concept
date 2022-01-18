###################################################
# .---. .----..----..-..-..---..---. 
# | |-< | || || || | \  / | |- | |-< 
# `-'`-'`----'`----'  `'  `---'`-'`-
###################################################
import httpx 
import os
from Resources import coloring
from dotenv import load_dotenv
###################################################
def reap(target):
    load_dotenv()
    headers = {'authority': 'discord.com', 'accept': '*/*', 'accept-language': 'en-US,en;q=0.9', 'authorization': os.getenv('TOKEN'), 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36', 'x-discord-locale': 'en-GB', 'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk2LjAuNDY2NC4xMTAgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6Ijk2LjAuNDY2NC4xMTAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTA4OTI0LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=='}
    with open("Resources/Utils/Data/gcs.txt") as groups:
        fgroups = groups.read().split("\n")
        if len(fgroups) != 0:
          added = 0
          for group in fgroups:
              h = httpx.put(f"https://discord.com/api/v9/channels/{group}/recipients/{target}", headers=headers)
              if h.status_code == 200 or h.status_code == 204:
                added += 1
                print(f"{coloring.GREEN}\n  <───$:[Added Target to Group {added}]───>") 
              else:
                added += 1
                print(h.json())
                print(f"{coloring.FAIL}\n  <───$:[Failed To Add Target to Group {added}]───>")
###################################################
