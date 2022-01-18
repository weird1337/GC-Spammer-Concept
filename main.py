###################################################
#__________                                 
#\______   \ ____   _______  __ ___________ 
# |       _//  _ \ /  _ \  \/ // __ \_  __ \
# |    |   (  <_> |  <_> )   /\  ___/|  | \/
# |____|_  /\____/ \____/ \_/  \___  >__|   
# 
# By: Roover & Shell | Message from the Developer:
###################################################
#                  # Warning #                    #
#   Don't edit any of the code below unless you know exactly what you are doing. I am not responsible for any alterations to the script and their affects on it's functions. I will not refund you if you break the bot's code so be mindful. #
###################################################
# Critical Imports & Functions #
###################################################
def warn(*args, **kwargs):
  pass
###################################################
import os
from Resources import *
from datetime import datetime
###################################################
try:
  import warnings
  warnings.warn = warn
except:
  print(f"{coloring.FAIL}  [Import Fail | Quitting... ]{coloring.WHITE}")
  os._exit(1)
###################################################
def main():
  inascii()
  while True:
    selection = input(f"""\n{coloring.BLUE}  ┌──{coloring.BLUE}「{coloring.FAIL}[Ω]RooverNET{coloring.BLUE}」-[{coloring.WARNING}!{coloring.BLUE}]{coloring.WHITE}:{coloring.BLUE}
  └─{coloring.HEADER}${coloring.WHITE}: """)
###################################################
    if selection.lower()[0:4] == "help":
      print(f"""
  {coloring.WHITE}--------------------------------------------------
  [{coloring.WARNING}!{coloring.WHITE}] Commands: {coloring.BLUE}[command name] [extra args]{coloring.WHITE}
  {coloring.BLUE}Name:          {coloring.BLUE}Description:
  
  {coloring.WARNING}create [#]  {coloring.WHITE}Creates specified number of GCs with tokens.
  {coloring.WARNING}reap [ID]    {coloring.WHITE}Spams specified target into GC.
  {coloring.WARNING}ascii       {coloring.WHITE}Sends terminal art.
  {coloring.WARNING}clear       {coloring.WHITE}Clears terminal.
  {coloring.WARNING}exit        {coloring.WHITE}Terminates script.
  {coloring.WARNING}filter      {coloring.WHITE}Filters tokens.
  --------------------------------------------------
""")
    elif selection.lower()[0:5] == "ascii":
      os.system('cls' if os.name=="nt" else 'clear')
      inascii()
    elif selection.lower()[0:5] == "clear":
      os.system('cls' if os.name=="nt" else 'clear')
    elif selection.lower()[0:4] == "exit":
      os._exit(2)
    elif selection.lower()[0:4] == "reap":
      try:
        target = selection.split("reap ")[1]
        reap(target)
      except:
        print(f"{coloring.FAIL}\n  <───$:[Invalid Input Entered]───>")
    elif selection.lower()[0:6] == "create":
      if os.stat("Resources/Utils/Data/tokens.txt").st_size == 0: # Checks for tokens in the tokens.txt file.
        os.system("cls" if os.name == "nt" else "clear")
        inascii()
        print(f"{coloring.FAIL}\n  <───$:[No Worker Tokens Provided]───>")
        quit()
      else:
        try:  
          count = int(selection.split("create ")[1])
          mine(count).work() # Starts mass creating group chats.
        except:
          print(f"{coloring.FAIL}\n  <───$:[Invalid Input Entered]───>")
    elif selection.lower()[0:6] == "filter": # Checks tokens for validity.
      if os.stat("Resources/Utils/Data/tokens.txt").st_size == 0: # Checks for tokens in the tokens.txt file.
        os.system("cls" if os.name == "nt" else "clear")
        inascii()
        print(f"{coloring.FAIL}\n  <───$:[No Worker Tokens Provided]───>")
        quit()
      else:
        miners().filter() # Starts filtering token list.
    else:
        pass
################################################### 
if __name__ == '__main__':
  os.system('cls' if os.name=="nt" else 'clear')
  the_time = datetime.now()
  current_time = the_time.strftime("%D")
  if os.name == "nt":
    os.system(f'title The Reaper : {str(current_time)}')
  main()