"""
Programmed by Hans-Günter Klemp 19.05.2026
programming language: Python
funktion1: Get themes of suggestion
funktion2: Get text from url
""" # Linda: <3

import wikipedia

def wiki_themesearch(suggestion):
    """Returns 5 Themes from the Wikipedia API"""
    error_counter = 0
    last_error = None

    wikipedia.set_lang("en")

    if not suggestion:
        suggestion = "None"

    while error_counter < 5:
        try:
            titles = wikipedia.search(suggestion, results = 5)
            return titles
 
        except Exception as e:
            error_counter += 1
            last_error = e

    return f"Fehler nach 5 Versuchen: {last_error}"



def wiki_text(title):
    """Returns the text of the Wikipedia page"""
    error_counter = 0
    last_error = None

    wikipedia.set_lang("en")
    while error_counter <= 5:
        try:
            text = wikipedia.page(title).content

        except ConnectionError:
            error_counter += 1
            if error_counter <= 5:
                return "Fehler: Keine Internetverbindung"

        except Exception as e:
            error_counter += 1
            if error_counter <= 5:
                return f"Fehler: {e}"

        else:
            return text

###Dean
### Were the requirement that you HAVE to use the WikiAPi or that you CAN use the api if you choose ?
### be carefull that you do not disqualify yourselves by not complying with the requirements

### Günter
### functions changed to wikiapi requests
