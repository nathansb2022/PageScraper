#!/usr/bin/env python3

#Time to page scrape artificialintelligence-news.com
#Works to gather text from the html of the URL and displays the results
#USE: python3 pagescraperAINews.py
#     python3 pagescraperAINews.py y
#INSTALL
#sudo pip3 install espeak rainbowtext PyAudio bs4
import requests, sys, pyttsx3, rainbowtext, os, time
from colorama import Fore
from bs4 import BeautifulSoup
site = "https://www.artificialintelligence-news.com/"
# Do you want a verbal response. Can be passed as a cmd line argument
def audioOrNot(site):
	if not len(sys.argv) > 1:
		i = input(Fore.GREEN + 'Do you want a verbal response? (y/n) ')
		if i == 'y':
			startIt(site)
		elif i == 'n':
			scrape(site)
		else:
			print(Fore.RED + 'Error occured')
	elif sys.argv[1] == 'y':
		startIt(site)
	elif sys.argv[1] == 'n':
		scrape(site)
	else:
		print(Fore.RED + 'Error occured')
# Pull the text from the html and print out
def scrape(site):
	r = requests.get(site)
	html = r.text
	soup = BeautifulSoup(html, "html.parser")
	lines = soup.body.get_text().strip()
	with open("filename","xt") as fd:
		for line in lines:
			fd.write(line)
		fd.close()
	with open("filename", "r+") as fd:
		fileLines = fd.readlines()
		fd.seek(0)
		fd.truncate()
		fd.writelines(fileLines[335:-305])
		fd.close()
	with open('filename', 'r') as fd:
		what_say = fd.read()
		fd.close()
	outtie = rainbowtext.text(what_say)
	preFace = "\n Artificial Intelligence News \n"
	print(preFace + outtie)
	return preFace + what_say
# Speak the contents gathered by scrape()
def startIt(site):
	engine = pyttsx3.init()
	engine.setProperty('rate', 135)
	engine.say(scrape(site))
	engine.runAndWait()
if __name__ == "__main__":
	audioOrNot(site)
	os.remove("filename")
