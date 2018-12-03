import json
import re
import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    response = requests.get("https://zh.flightaware.com/live/map")
    response.enconding = "utf-8"
    text = response.text
    soup = BeautifulSoup(text, "html.parser")

    print(soup.prettify)

    pattern = re.compile(r"var mapGlobals = .*?", re.MULTILINE | re.DOTALL)
    script = soup.find("script", text=pattern)
    print(script)

    if script:
        pattern = re.compile(r"\"VICINITY_TOKEN\":\"(((\d)|[a-z])*)\"", re.MULTILINE | re.DOTALL)
        match = pattern.search(script.text)
        if match:
            print(match.group(1))
    #print(response.text)
'''
    print(response.cookies)
VICINITY_TOKEN
    print(response.content)
    print(response.content.decode("utf-8"))
'''