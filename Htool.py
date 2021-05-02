import os,sys
from os import system
import random
from time import sleep
from core.tools import *
R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
B = "\033[1;34m"
P = "\033[1;35m"
W = "\033[1;37m"
L = "\033[1;32;4m"
O = "\033[0m"
sleep(1)
os.system("clear")
sleep(0.5)
colors = [Y,B,G,R,P]
logo = """
         $$\   $$\      $$$$$$$$\                  $$\
         $$ |  $$ |     \__$$  __|                 $$ |
         $$ |  $$ |        $$ | $$$$$$\   $$$$$$\  $$ |
         $$$$$$$$ |$$$$$$\ $$ |$$  __$$\ $$  __$$\ $$ |
         $$  __$$ |\______|$$ |$$ /  $$ |$$ /  $$ |$$ |
         $$ |  $$ |        $$ |$$ |  $$ |$$ |  $$ |$$ |
         $$ |  $$ |        $$ |\$$$$$$  |\$$$$$$  |$$ |
         \__|  \__|        \__| \______/  \______/ \__|

         >>>>>>>>>>>>>>> Hacking Tools <<<<<<<<<<<<<<<<"""

A = random.choice(colors)
print(A+logo)
print("\t{} >>>>>>>>>>>>> Total Tools = {}308{}{} <<<<<<<<<<<<<<{}".format(A,L,O,A,O))
print("\t\t {} Thanks to {}Prudhvi{}{} and {}Rokuro{}".format(A,L,O,A,L,O))
sleep(0.5)
def main():
  print ("""\n
  {}[{}1{}]{} Phishing Tools
  {}[{}2{}]{} Brute Forcing Tools
  {}[{}3{}]{} Cloning Tools
  {}[{}4{}]{} Vulnerability Scanning Tools
  {}[{}5{}]{} Information Gathering Tools
  {}[{}6{}]{} Tracing and Tracking Tools
  {}[{}7{}]{} Exploitation Tools
  {}[{}8{}]{} Password Cracking Tools
  {}[{}9{}]{} Wifi Hacking Tools
  {}[{}10{}]{} Bombing Tools
  {}[{}11{}]{} DDOS Tools
  {}[{}12{}]{} Malware Tools
  {}[{}13{}]{} Termux Special Packages
  {}[{}14{}]{} Another Hacking Tools
  {}[{}00{}]{} Exit\n """
  .format(R,W,R,G,R,W,R,G,R,W,R,G,R,W,R,G,R,W,R,G,R,W,R,G,R,W,R,G,R,W,R,G,R,W,R,G,R,W,R,G,R,W,R,G,R,W,R,G,R,W,R,G,R,W,R,G,R,W,R,G))


main()
def Anon():
  try:
   x = input("{} [{}*{}] Select Option : {}".format(W,A,W,A))
  except KeyboardInterrupt:
   print(O)
   exit()
  sleep(1)
  system("clear")
  if x == "1" or x == "01":
     Phish()
     Restart()
  elif x == "2" or x == "02":
     Brute()
     Restart()
  elif x == "3" or x == "03":
     Clone()
     Restart()
  elif x == "4" or x == "04":
     Vuln()
     Restart()
  elif x == "5" or x == "05":
     Info()
     Restart()
  elif x == "6" or x == "06":
     Trac()
     Restart()
  elif x == "7" or x == "07":
     Exp()
     Restart()
  elif x == "8" or x == "08":
     Pass()
     Restart()
  elif x == "9" or x == "09":
     Wifi()
     Restart()
  elif x == "10":
     Bom()
     Restart()
  elif x == "11":
     DDOS()
     Restart()
  elif x == "12":
     Mal()
     Restart()
  elif x == "13":
     Special()
     Restart()
  elif x == "14":
     Ano()
     Restart()
  elif x == "0" or x == "00":
     exit()
  else:
     BackToMenu()
Anon()
