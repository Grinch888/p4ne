import json, pprint, requests, glob
from time import sleep


def cardlist(files):
    cards = []
    for f in files:
        with open(f) as file:
            config = json.load(file)
            for s in config:
                cards.append(s['CreditCard']['CardNumber'])
    return cards

def converter(cards):
    cardsc = []
    for i in cards:
        i = str(i)
        cardsc.append(i[0:8])
    return cardsc

def checkcards(cardsc):
    for i in cardsc:
        URL = "https://lookup.binlist.net/"
        URL = URL + i
        r = requests.get(URL, headers={'Accept-version': "3"})
#        print(r)
#        print(type(r.status_code))
#        print(not (r.status_code == 404))
        if (r.status_code == 200):
            obj = json.loads(r.content.decode())
            print(i + " " + obj['bank']['name'])
        sleep(2)
    return print(obj['bank']['name'])

cards = converter(cardlist(glob.glob("*.json")))

checkcards(cards)