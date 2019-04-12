import json, requests, glob
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
    l = []
    for i in cardsc:
        URL = "https://lookup.binlist.net/"
        URL = URL + i
        r = requests.get(URL, headers={'Accept-version': "3"})

        if (r.status_code == 200):
            obj = json.loads(r.content.decode())
            print(type(obj['bank']['name']))
            if 'name' in obj['bank']:
                i = obj['bank']['name']
                l = l.append(i)
#                print(i + " " + obj['bank']['name'])
#                print(len(l))
#        sleep(1)
    return (l)

cards = converter(cardlist(glob.glob("*.json")))

l = checkcards(cards)
for i in l:
    print(i)