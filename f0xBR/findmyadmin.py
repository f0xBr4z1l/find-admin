#!/usr/bin/python3
#CRIADO POR BR huehuehuehue
#Manda um abraço para o fox :D
import urllib.request
import sys
#cores
verde = '\033[1;32m'

red = '\033[1;31m'

azul = '\033[1;34m'

print(azul+"""███████╗ ██████╗ ██╗  ██╗        ██████╗ ██████╗ 
██╔════╝██╔═████╗╚██╗██╔╝        ██╔══██╗██╔══██╗
█████╗  ██║██╔██║ ╚███╔╝         ██████╔╝██████╔╝
██╔══╝  ████╔╝██║ ██╔██╗         ██╔══██╗██╔══██╗
██║     ╚██████╔╝██╔╝ ██╗███████╗██████╔╝██║  ██║
╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝  ╚═╝
                                                 """)
print(verde+"CADE O ADMIN?")

try:
    url = sys.argv[1]
except:
       print(red+"digite o alvo \n ex testphp.vulnweb.com")
       exit()
alvo = "http://"+url+"/"

f = open("word/word.txt", "r")

while True:
      a = f.readline()
      if not a:
         break
      else:
           urll2 = alvo+a
           try:
               urllib.request.urlopen(urll2)
               print(verde+"alvo encontrado ",urll2)
               break
               exit()
           except:
                  print(red+"404 não localizado",urll2)
