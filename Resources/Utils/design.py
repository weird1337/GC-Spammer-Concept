###################################################
#.---. .----..----..-..-..---..---. 
#| |-< | || || || | \  / | |- | |-< 
#`-'`-'`----'`----'  `'  `---'`-'`-'
###################################################
from colorama import Fore as C
###################################################
class coloring:

    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    WHITE = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
###################################################
def inascii():
  print(f"""
  {C.RED}██████{C.BLUE}╗{C.RED}░███████{C.BLUE}╗{C.RED}░█████{C.BLUE}╗{C.RED}░██████{C.BLUE}╗{C.RED}░███████{C.BLUE}╗{C.RED}██████{C.BLUE}╗{C.RED}░
  ██{C.BLUE}╔══{C.RED}██{C.BLUE}╗{C.RED}██{C.BLUE}╔════╝{C.RED}██{C.BLUE}╔══{C.RED}██{C.BLUE}╗{C.RED}██{C.BLUE}╔══{C.RED}██{C.BLUE}╗{C.RED}██{C.BLUE}╔════╝{C.RED}██{C.BLUE}╔══{C.RED}██{C.BLUE}╗{C.RED}
  ██████{C.BLUE}╔╝{C.RED}█████{C.BLUE}╗{C.RED}░░███████{C.BLUE}║{C.RED}██████{C.BLUE}╔╝{C.RED}█████{C.BLUE}╗{C.RED}░░██████{C.BLUE}╔╝
  {C.RED}██{C.BLUE}╔══{C.RED}██{C.BLUE}╗{C.RED}██{C.BLUE}╔══╝{C.RED}░░██{C.BLUE}╔══{C.RED}██{C.BLUE}║{C.RED}██{C.BLUE}╔═══╝{C.RED}░██{C.BLUE}╔══╝{C.RED}░░██{C.BLUE}╔══{C.RED}██{C.BLUE}╗
  {C.RED}██{C.BLUE}║{C.RED}░░██{C.BLUE}║{C.RED}███████{C.BLUE}╗{C.RED}██{C.BLUE}║{C.RED}░░██{C.BLUE}║{C.RED}██{C.BLUE}║{C.RED}░░░░░███████{C.BLUE}╗{C.RED}██{C.BLUE}║{C.RED}░░██{C.BLUE}║
  ╚═╝{C.RED}░░{C.BLUE}╚═╝╚══════╝╚═╝{C.RED}░░{C.BLUE}╚═╝╚═╝{C.RED}░░░░░{C.BLUE}╚══════╝╚═╝{C.RED}░░{C.BLUE}╚═╝
      By: Roover @ Omega Development
  """)
  print("  " + f"{C.MAGENTA}━"*65)
###################################################