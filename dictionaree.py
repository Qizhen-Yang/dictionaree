import requests
from bs4 import BeautifulSoup
import os
from time import sleep

i = []
a = input()
i.append(a)
while a.lower() != "eof":
    a = input()
    i.append(a)
i.pop()

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36", 
         "Cookie": "your cookie"}
d = []
for word in i:
    result = requests.get("https://www.bing.com/dict/search?q=" + word, headers=header)
    result_bs = BeautifulSoup(result.text, "html.parser")
    newitem = result_bs.find_all("div", attrs = {'class': 'hd_area'}) + result_bs.find_all("span", attrs = {'class': 'def b_regtxt'})
    if len(newitem) < 2:
        d.append([word, "<br/> No definitions"])
        print("Failed to find definition of:", word)
    else:
        d.append(newitem)
        print("Added word:", word)

f = open("Dictionaree.html", "w+", encoding = "utf-8")
f.write("<meta charset='utf-8'/><style>*{font-size:16px;line-height:36px;}html{margin:auto;text-align:center;max-width:21cm;}hr{width:50%;}</style>")
for word_def in d:
    for j in word_def:
        f.write(str(j))
    f.write("<hr/>")
f.close()
print("Generated file: Dictionaree.html")
os.startfile("Dictionaree.html")
sleep(5)
os.remove("Dictionaree.html")