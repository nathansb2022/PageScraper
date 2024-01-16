#!/usr/bin/env python3

#Time to page scrape thhackernews.com
#Works to gather text from the html of the URL and displays the results
#USE: python3 pagescraperTHN.py
#     python3 pagescraperTHN.py y
#INSTALL
#sudo pip3 install espeak rainbowtext PyAudio bs4
import requests, sys, pyttsx3, rainbowtext, os, time
from colorama import Fore
from bs4 import BeautifulSoup
from openai import OpenAI
# Add in your environment variable name for OPENAI_API_KEY
client = OpenAI(
   api_key = os.environ.get('OKEY'),
 )
site = "https://thehackernews.com"
# In system role modify your cyber assistant to your specifications
def get_completion(prompt):
	completion = client.chat.completions.create(
	  model="gpt-4-1106-preview",
	  messages=[
	    {"role": "system", "content": "You are a Cybersecurity assistant, skilled in explaining complex cybersecurity challenges, \
		threats, recommendations, and remediations. Sift the information provided, takeaway the highlights, and summarize the \
		content in a professional format. Please put in a paragraph format as if you were to read it to someone. Be professional \
		and funny."},
	    {"role": "user", "content": prompt}
	  ]
	)
	return completion.choices[0].message.content

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
	filename = "THN_" + time.strftime("%Y%m%d") + ".txt"
	with open(filename,"xt") as fd:
		for line in lines:
			fd.write(line)
		fd.close()
	with open(filename, "r+") as fd:
		fileLines = fd.readlines()
		fd.seek(0)
		fd.truncate()
		fd.writelines(fileLines[110:-270])
		fd.close()
	with open(filename, 'r') as fd:
		what_say = fd.read()
		fd.close()
	cgpt = get_completion(what_say)
	outtie = rainbowtext.text(cgpt)
	preFace = "\n From The Hacker News, Number 1 Trusted Cybersecurity News platform and summarized with ChatGPT. \n"
	print(preFace + outtie)
	return preFace + cgpt
# Speak the contents gathered by scrape()
def startIt(site):
	engine = pyttsx3.init()
	engine.setProperty('rate', 135)
	engine.say(scrape(site))
	engine.runAndWait()
if __name__ == "__main__":
	audioOrNot(site)
