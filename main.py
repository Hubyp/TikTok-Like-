mport sys
from time import sleep
import colorama
from colorama import Fore
from colorama import Style

print("""
 ______   __     __  __        ______   ______     __  __                 
/\__  _\ /\ \   /\ \/ /       /\__  _\ /\  __ \   /\ \/ /                 
\/_/\ \/ \ \ \  \ \  _"-.     \/_/\ \/ \ \ \/\ \  \ \  _"-.               
   \ \_\  \ \_\  \ \_\ \_\       \ \_\  \ \_____\  \ \_\ \_\              
    \/_/   \/_/   \/_/\/_/        \/_/   \/_____/   \/_/\/_/    

 __         __     __  __     ______        ______     ______     ______  
/\ \       /\ \   /\ \/ /    /\  ___\      /\  == \   /\  __ \   /\__  _\ 
\ \ \____  \ \ \  \ \  _"-.  \ \  __\      \ \  __<   \ \ \/\ \  \/_/\ \/ 
 \ \_____\  \ \_\  \ \_\ \_\  \ \_____\     \ \_____\  \ \_____\    \ \_\ 
  \/_____/   \/_/   \/_/\/_/   \/_____/     \/_____/   \/_____/     \/_/ 
""")
words = "Verson 1.0\n\n"

for char in words:
    sleep(0.2)
    sys.stdout.write(char)
    sys.stdout.flush()
  
input(Fore.BLUE + "⇦  Video link ⇨  ")

amount = input(Fore.BLUE + "⇦  amount ⇨  ")

increment = 1

while int(amount) > increment > 0:
    sleep(0.01)
    print (Fore.MAGENTA + 'Sent' + Fore.CYAN, ' like:',  Style.NORMAL, '|', increment, '|')
    increment = increment + 1
print(Fore.RED, "Faild 1 Like")
print(Fore.GREEN, "  !succses!")
