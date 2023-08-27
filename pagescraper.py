#!/usr/bin/env python3

#Time to page scrape
#Works to gather text from the html of the URL and displays the results
#USE: python3 pagescraper.py
#     python3 pagescraper.py https://www.google.com
#     python3 pagescraper.py https://www.google.com y
#INSTALL
#sudo pip3 install espeak rainbowtext PyAudio
import requests, sys, pyttsx3, rainbowtext
from colorama import Fore
from bs4 import BeautifulSoup
# Do you want a verbal response. Can be passed as a cmd line argument
def audioOrNot(site):
    if not len(sys.argv) > 2:
        i = input(Fore.GREEN + 'Do you want a verbal response? (y/n) ')
        if i == 'y':
            startIt(site)
        elif i == 'n':
            scrape(site)
        else:
            print(Fore.RED + 'Error occured')
    elif sys.argv[2] == 'y':
        startIt(site)
    elif sys.argv[2] == 'n':
        scrape(site)
    else:
        print(Fore.RED + 'Error occured')
# Check if the url was passed as a cmd line argument
def checkURL():
    if not len(sys.argv) > 1:
        site = input(Fore.GREEN + "Please input your URL: ")
        return site
    else:
    	site = sys.argv[1]
    	return site
# Pull the text from the html and print out
def scrape(site):
    r = requests.get(site)
    html = r.text
    soup = BeautifulSoup(html, "html.parser")
    print(rainbowtext.text(soup.body.get_text().strip()))
    return str(soup.body.get_text().strip())
# Speak the contents gathered by scrape()
def startIt(site):

	engine = pyttsx3.init()
	engine.setProperty('rate', 120)
	engine.say(scrape(site))
	engine.runAndWait()
if __name__ == "__main__":
    site = checkURL()
    audioOrNot(site)
