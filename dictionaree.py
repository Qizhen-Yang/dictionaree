import requests
from bs4 import BeautifulSoup
import os
from time import sleep
import string

import youdao
import collins

VERSION = "v0.3.4"

def help():
	print("Dictionaree commands:")
	print("exit, e\t\tExit the program")
	print("help, h\t\tProvide information about Dictionaree commands")
	print("add, a\t\tStart inputting words, Type `eof` to end")
	print("dict, d\t\tChoose dictionaries")
	print("\t\ty: Youdao (en <-> zh_cn)")
	print("\t\tc: Collins (en <-> en)")
	print("\t\tb: Both dictionaries")
	print("generate, g\tGenerate `dictionaree.html`")
	print("version, v\tShow version information")
	print("clear, c\tClear saved list of words")

def cmdToAbbr(text: str) -> str:
	cmds = {
		"exit": "e",
		"help": "h",
		"add": "a",
		"dict": "d",
		"generate": "g",
		"version": "v",
		"clear": "c"
	}
	r = cmds.get(text, None)
	if (r):
		return r
	else:
		return text

print("Dictionaree", VERSION)
print("Copyright (c) 2021 Qizhen Yang")
print("Dictionaree is a FREE software.")
print(" *  GitHub repo: Qizhen-Yang/dictionaree")
print(" *  License: MIT License\n")

print("\nType `h` for help.\n")

if (os.path.isfile("config")):
	config = open("config", "r+", encoding = "utf-8")
	dictionary = config.readline()
	if (dictionary == "y"):
		print("Using dictionary: Youdao (en <-> zh_cn)")
	elif (dictionary == "c"):
		print("Using dictionary: Collins (en <-> en)")
	else:
		dictionary = "b"
		print("Using both dictionaries")
else:
	config = open("config", "w+", encoding = "utf-8")
	config.write("b")
	dictionary = "b"
	print("Using both dictionaries")

i = []
d = []

while (1):
	cmd = input("> ").lower().strip()
	if (cmd == ""):
		continue
	kw = cmdToAbbr(cmd.split()[0])
	if (kw == "e"):
		config.close()
		os._exit(0)
	elif (kw == "h"):
		help()
	elif (kw == "a"):
		i = []
		a = input("Add a word > ").lower()
		i.append(a)
		while a != "eof":
			a = input("Add a word > ").lower()
			i.append(a)
		i.pop()
		print("End of inputting.\n")
		if (dictionary == "y"):
			for word in i:
				d.append([word, youdao.search(word)])
		elif (dictionary == "c"):
			for word in i:
				d.append([word, collins.search(word)])
		else:
			for word in i:
				d.append([word, youdao.search(word) + "<br/>" + collins.search(word)])
		print("Done.")
	elif (kw == "d"):
		if (len(cmd.split()) <= 1):
			print("dict, d\tChoose dictionaries")
			print("\ty: Youdao (en <-> zh_cn)")
			print("\tc: Collins (en <-> en)")
			print("\tb: Both dictionaries")
		elif (cmd.split()[1] == "y"):
			dictionary = "y"
			print("Using dictionary: Youdao (en <-> zh_cn)")
		elif (cmd.split()[1] == "c"):
			dictionary = "c"
			print("Using dictionary: Collins (en <-> en)")
		elif (cmd.split()[1] == "b"):
			dictionary = "b"
			print("Using both dictionaries")
		else:
			print("Unknown dictionary `%s`" % cmd.split()[1])
		config.seek(0)
		config.truncate()
		config.write(dictionary)
	elif (kw == "g"):
		if (d == []):
			print("Nothing to show. XD")
		else:
			f = open("Dictionaree.html", "w+", encoding = "utf-8")
			f.write("<!DOCTYPE html><html><head><meta charset='utf-8'/><title>Vocabulary List</title></head><body class='vscode-body vscode-light'>")
			f.write("""<style>
				html {
					margin: auto;
					max-width: 21cm;
				}
				* {
					font-family: 'Open Sans', 'Segoe UI', sans-serif;
				}
				*:not(h1) {
					font-size: 16px;
				}
				table tr td:first-child, a, a:hover, a:visited {
					font-weight: 600;
					color: #FFC408;
					vertical-align: top;
				}
				table tr td:first-child {
					padding-top: 24px;
				}
				.baav {
					font-weight: 400;
					margin-top: 16px;
				}
				</style>""")
			f.write("""<style>
				.additional,.more-example,.collapse-content,.wt-collapse,#webPhrase,.sp,.sensenum,.cit,.xr,.title_frequency_container,.copyright,.entry_title,.thes,.keyword,.orth:first-of-type,.exampleLists,.tabs,h4,.collinsOrder {
					display: none;
				}
				span.additional:first-of-type {
					display: block;
					text-transform: uppercase;
					border-bottom: 1px solid #000000;
					width: fit-content;
				}
				</style>""")
			f.write("<link rel='stylesheet' href='https://cdn.jsdelivr.net/gh/Microsoft/vscode/extensions/markdown-language-features/media/markdown.css'>")
			f.write("<h1>Vocabulary List</h1><table>")
			for word_def in d:
				f.write("<tr>")
				for item in word_def:
					f.write("<td>")
					for item_ in item:
						f.write(str(item_))
					f.write("</td>")
				f.write("</tr>")
			f.write("</table>")
			f.write("<p>Generated by <a href='https://github.com/Qizhen-Yang/dictionaree'>Dictionaree</a>, a great work by Qizhen Yang.</p>")
			f.write("</body></html>")
			f.close()
			print("Generated file: Dictionaree.html")
			os.startfile("Dictionaree.html")
	elif (kw == "v"):
		print(VERSION)
	elif (kw == "c"):
		i = []
		d = []
		print("Cleared current word list")
	else:
		print("Unknown command `%s`" % kw)