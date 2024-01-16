# PageScraper

Python script to gather the text of a html web page and display it in the console. Addtitionally, has the ability to speak the provided text. There is "The Hacker News" rendition in theHackerNews folder and "Artificial Intelligence News" is in the artificialintelligence-news folder.

## theHackerNews Folder

This folder contains a python file that scrapes thehackernews.com and then passes the data to ChatGPT API to summarize the page. The data from thehackernews.com and summary from ChatGPT is saved in working directory THN_yyymmdd.txt.

### Example usage of pagescraperTHN.py

The Hacker News
```bash
python3 pagescraperTHN.py
```
## Terminal Output

First, the terminal may request the URL or ask for the text to be spoken. Page text will appear in rainbowtext and can be removed from the scrape() function. Tested on Ubuntu.

## How to Use Rest of the Files

Example Usage:

Add URL as argument and y/n for verbal response
```bash
python3 pagescraper.py https://www.cnet.com/news/ n
```
Or pipe it to tee command to store in a text file
```bash
python3 pagescraper.py https://www.cnet.com/news/ n | tee news_9_20_23.txt
```
Or without any arguments
```bash
python3 pagescraper.py
```
Artificial Intelligence News
```bash
python3 pagescraperAINews.py y
```
## Install Requirements

To grab python requirements do:
```bash
sudo pip3 install espeak rainbowtext PyAudio bs4 openai
```
# Links

[The Hacker News](https://thehackernews.com)

[Artificial Intelligence News](https://www.artificialintelligence-news.com/)
