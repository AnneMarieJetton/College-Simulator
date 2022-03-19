from characters import Erik
from characters import Mono
from characters import viki
from characters import Vladimir

def getQuotes(level):
    if level == 0:
        return Erik.getQuotes()
    if level == 1:
        return viki.getQuotes()
    if level == 2:
        return Mono.getQuotes()
    if level == 3:
        return Vladimir.getQuotes()

def getSprite(level):
    if level == 0:
        return Erik.getArt()
    if level == 1:
        return viki.getArt()
    if level == 2:
        return Mono.getArt()
    if level == 3:
        return Vladimir.getArt()