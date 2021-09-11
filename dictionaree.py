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
    result = requests.get("http://youdao.com/w/eng/" + word, headers=header)
    result_bs = BeautifulSoup(result.text, "html.parser")
    newitem = str(result_bs.find("h2", attrs = {'class': 'wordbook-js'}))
    if newitem == "None":
        d.append([word, "<br/> No definitions"])
        print("Failed to find definition of:", word)
    else:
        newitem += str(result_bs.find("div", attrs = {'class': 'trans-container'}))
        d.append(newitem)
        print("Added word:", word)

f = open("Dictionaree.html", "w+", encoding = "utf-8")
f.write("<meta charset='utf-8'/><style>*{font-size:16px;}.word{margin:auto;width:fit-content;text-align:center;}.baav{font-weight:400;margin-top:16px;}html{margin:auto;max-width:21cm;}hr{width:50%;}.additional{display:none;}</style>")
for word_def in d:
    f.write("<div class='word'>")
    for j in word_def:
        f.write(str(j))
    f.write("</div><hr/>")
f.close()
print("Generated file: Dictionaree.html")
os.startfile("Dictionaree.html")
sleep(5)
os.remove("Dictionaree.html")