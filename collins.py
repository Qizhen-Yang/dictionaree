import requests
from bs4 import BeautifulSoup

def search(word):
	header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36", "Cookie": "Collins"}
	result = requests.get("http://youdao.com/w/eng/" + word, headers=header)
	result_bs = BeautifulSoup(result.text, "html.parser")
	newitem = str(result_bs.find("span", attrs = {"class": "title"}))
	if newitem == "None":
		d = "<p>[Collins] No definitions</p>"
		print("[Collins]\tNo def of:\t", word)
	else:
		newitem = str(result_bs.find("div", attrs = {'id': 'authTrans'}))
		newitem = newitem.replace("<ul", "<div")
		newitem = newitem.replace("</ul>", "</div>")
		newitem = newitem.replace("<li>", "<p>")
		newitem = newitem.replace("</li>", "</p>")
		newitem = newitem.replace("<a", "<span")
		newitem = newitem.replace("</a>", "</span>")
		d = newitem
		print("[Collins]\tAdded word:\t", word)
	return d