"""
Programmed by Hans-Günter Klemp 19.05.2026
programming language: Python
function 1: Get random Wikipedia page
function 2: Get themes of suggestion
function 3: Get text from url
""" # Linda: <3

import wikipediaapi
import random

def wiki_random():
    """Returns a random Wikipedia page"""

    wiki = wikipediaapi.Wikipedia(
        language="en",
        user_agent="WikiTool/1.0 (learning project)"
    )
    result = []
    pages = wiki.random(limit=5)

    return list(pages.keys())

def wiki_themesearch(suggestion):
    """Returns 5 Themes from the Wikipedia API"""

    wiki = wikipediaapi.Wikipedia(
        language="en",
        user_agent="WikiTool/1.0 (learning project)"
    )

    if not suggestion:
        suggestion = "Wikipedia"

    results = wiki.search(suggestion, limit = 5)

    return list(results.pages.keys())


def wiki_text(title):
    """Returns the text of the Wikipedia page"""

    wiki = wikipediaapi.Wikipedia(
        language="en",
        user_agent="WikiTool/1.0 (learning project)"
    )

    page = wiki.page(title)

    if not page.exists():
        return ["Fehler", "Seite nicht gefunden"]

    return page.text


