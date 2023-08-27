# PageScraper
Python script to gather the text of a html web page and display it in the console. Addtitionally, has the ability to speak the provided text. Tested on Debian Distribution.

# Terminal Output

First, the terminal may request the URL or ask for the text to be spoken. Page text will appear in rainbowtext and can be removed from the scrape() function.

# How to Use

Example Usage:

Add URL as argument and y/n for verbal response
```bash
python3 pagescraper.py 10.10.10.10 n
```
Or without
```bash
python3 pagescraper.py
```
# Install Requirements

To grab python requirements do:
```bash
sudo pip3 install espeak rainbowtext PyAudio
```
