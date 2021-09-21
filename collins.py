import requests
from bs4 import BeautifulSoup

def search(word):
	header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36", "Cookie": "your cookie"}
	result = requests.get("https://www.collinsdictionary.com/dictionary/english/" + word, headers=header)
	result_bs = BeautifulSoup(result.text, "html.parser")
	newitem = str(result_bs.find("h2", attrs = {'class': 'h2_entry'}))
	if newitem == "None":
		d = ["<div class='nodef'><strong>", word, "</strong><br/><br/> No definitions </div>"]
		print("Failed to find definition of:", word)
	else:
		newitem = str(result_bs.find("div", attrs = {'class': 'dictentry'}))
		newitem = newitem.replace("<a", "<span")
		newitem = newitem.replace("</a>", "</span>")
		d = newitem
		print("[Collins]", "Added word:", word)
	return d