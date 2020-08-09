import os,sys
import random
from termcolor import colored
from time import sleep
from core.tools import *
sleep(1)
os.system("clear")
sleep(1)
colors=['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[36m']
logo = """
           $$\   $$\      $$$$$$$$\                  $$\ 
           $$ |  $$ |     \__$$  __|                 $$ |
           $$ |  $$ |        $$ | $$$$$$\   $$$$$$\  $$ |
           $$$$$$$$ |$$$$$$\ $$ |$$  __$$\ $$  __$$\ $$ |
           $$  __$$ |\______|$$ |$$ /  $$ |$$ /  $$ |$$ |
           $$ |  $$ |        $$ |$$ |  $$ |$$ |  $$ |$$ |
           $$ |  $$ |        $$ |\$$$$$$  |\$$$$$$  |$$ |
           \__|  \__|        \__| \______/  \______/ \__|

           >>>>>>>>>>>>>>> Hacking Tools <<<<<<<<<<<<<<<<
           >>>>>>>>>>>>> Total Tools = 212 <<<<<<<<<<<<<<"""
print(random.choice(colors)+logo)
print ("\t\t\033[0m Thanks To " "\033[4m \033[1;32m Prudhvi \033[0m" "and" "\033[4m \033[1;32m Joyson \033[0m")
sleep(1)
def main():
  print ("""\033[1;32m \n
  [1] Phishing Tools
  [2] Brute Forcing Tools
  [3] Vulnerability Scanning Tools
  [4] Information Gathering Tools
  [5] Wifi Hacking Tools
  [6] Tracing and Tracking Tools
  [7] Exploitation Tools
  [8] Password Attacking Tools
  [9] Malware Tools
  [10] Bombing Tools
  [11] Another Hacking Tools
  [00] Exit\n""")
main()
def Anon():
  x = (input(colored("  [*] Select Option : ","white")))
  sleep(1)
  os.system("clear")
  sleep(1)
  if x == "1" or x == "01":
     Phish()
  elif x == "2" or x == "02":
     Brute()
  elif x == "3" or x == "03":
     Vuln()
  elif x == "4" or x == "04":
     Info()
  elif x == "5" or x == "05":
     Wifi()
  elif x == "6" or x == "06":
     Trac()
  elif x == "7" or x == "07":
     Exp()
  elif x == "8" or x == "08":
     Pass()
  elif x == "9" or x == "09":
     Mal()
  elif x == "10":
     Bom()
  elif x == "11":
     Ano()
  elif x == "00":
     print (os.system("cd core && rm -rf __pycache__"))
     exit()
Anon()

