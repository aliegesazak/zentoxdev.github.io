import pyautogui
import keyboard
import ctypes
import mss
from time import sleep
import sys
from termcolor import colored, cprint
import os
from colorama import Fore, Back, Style, init
import colorama, sys, time
import base64
import random

G_KEY = "g"

clear = lambda: os.system('cls')
title = lambda: os.system('title cCcaliegesazakcCc')

title()
clear()
colorama.init(autoreset=True)
bred = Fore.RED + Style.BRIGHT
red = Fore.RED
bos = "\033[1;37m"

z = """
			                        Version 1.0.0
                        [+] █████████████████████████████████████████████████████ [+]
                	                    Coded by aliegesazak\n\n"""
print("""

           ███████╗██████╗  █████╗     ██████╗ ██╗   ██╗ █████╗ ███╗   ██╗    ██╗  ██╗ █████╗  ██████╗██╗  ██╗
           ██╔════╝██╔══██╗██╔══██╗    ██╔══██╗██║   ██║██╔══██╗████╗  ██║    ██║  ██║██╔══██╗██╔════╝██║ ██╔╝
           █████╗  ██████╔╝███████║    ██████╔╝██║   ██║███████║██╔██╗ ██║    ███████║███████║██║     █████╔╝ 
           ██╔══╝  ██╔══██╗██╔══██║    ██╔═══╝ ██║   ██║██╔══██║██║╚██╗██║    ██╔══██║██╔══██║██║     ██╔═██╗ 
           ███████╗██████╔╝██║  ██║    ██║     ╚██████╔╝██║  ██║██║ ╚████║    ██║  ██║██║  ██║╚██████╗██║  ██╗
           ╚══════╝╚═════╝ ╚═╝  ╚═╝    ╚═╝      ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
                                                        /´¯/) 
                                                      ,/¯  / 
                                                     /    / 
                                               /´¯/'   '/´¯¯`·¸ 
                                            /'/   /    /       /¨¯\ 
                                          ('(   ´   ´     ¯~/'   ') 
                                           \                 '     / 
                                            ''   \           _.·´ 
                                              \              ( 
                                               \             \ """)

for c in z:
    sys.stdout.write(f"{bred}{c}")
    sys.stdout.flush()
    time.sleep(0.02)
while True:
 num = "1"
 secenek = input("Video hızlandırmasını açıp kapatmak için 1'i tuşla: ")
 if secenek == num:
    print('Lütfen eba sayfasına geçin!')
    sleep(2)
    pyautogui.press(G_KEY)
    print('Videonuz hızlandırıldı')
else:
    print('Hatalı Tuş')
sleep(1000000)