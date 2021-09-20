import requests
from bs4 import BeautifulSoup

def search(word):
	header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36", "Cookie": "your cookie"}
	result = requests.get("http://youdao.com/w/eng/" + word, headers=header)
	result_bs = BeautifulSoup(result.text, "html.parser")
	newitem = str(result_bs.find("h2", attrs = {'class': 'wordbook-js'}))
	if newitem == "None":
		d = ["<div class='nodef'><strong>", word, "</strong><br/><br/> No definitions </div>"]
		print("Failed to find definition of:", word)
	else:
		newitem += str(result_bs.find("div", attrs = {'class': 'trans-container'}))
		newitem = newitem.replace("<ul>", "<div>")
		newitem = newitem.replace("</ul>", "</div>")
		newitem = newitem.replace("<li>", "<p>")
		newitem = newitem.replace("</li>", "</p>")
		newitem = newitem.replace("<a", "<span")
		newitem = newitem.replace("</a>", "</span>")
		d = newitem
		print("Added word:", word, "[Youdao]")
	return d