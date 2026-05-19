"""
Programmed by Hans-Günter Klemp 19.05.2026
programming language: Python
funktion1: Get themes of suggestion
funktion2: get text from url
""" # Linda: <3

import requests

def wiki_themesearch(suggestion):
    # Sucht nach 5 Themen

    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "opensearch",
        "search": suggestion,
        "format": "json",
        "namespace": 0,
        "limit": 5
    }

    headers = {
        "User-Agent": "WikiTool/1.0 (learning project)"
    }

    response = requests.get(url, params = params, headers = headers, timeout = 10)

    # Fehler abfangen vom Server
    if response.status_code != 200:
        return f"HTTP Fehler: {response.status_code}"

    data = response.json()
    titles = data[1]

    return titles


def wiki_text(title, lang="en"):
#Holt den Text. ohne HTML Anteil

    url = f"https://{lang}.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "titles": title,
        "explaintext": True,   # entfernt HTML
        "redirects": 1         # folgt Weiterleitungen automatisch
    }

    headers = {
        "User-Agent": "WikiTool/1.0 (learning project)"
    }

    response = requests.get(url, params = params, headers = headers, timeout = 10)

    # Fehler abfangen vom Server
    if response.status_code != 200:
        return f"HTTP Fehler: {response.status_code}"

    data = response.json()

    pages = data["query"]["pages"]

    for value in pages.values():
        page = value
        break

    if "extract" in page:
        return page["extract"]

    return "Kein Text gefunden"

text_string = wiki_text("Bremen")

print(text_string)



""" @Thorsten: So müsste das gehen"""
###Dean
### Were the requirement that you HAVE to use the WikiAPi or that you CAN use the api if you choose ?
### be carefull that you do not disqualify yourselves by not complying with the requirements


