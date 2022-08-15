import random
import pandas as pd
from pathlib import Path

class card:
       def __init__(self, cardname,manaCost,cmc,colorIdentity ,typeline,text, power,toughness,types,subtypes): # , artist,, ,, rarity): #, ):
           self.cardname = cardname
           self.manaCost = manaCost
           self.cmc = cmc
           self.colorIdentity = colorIdentity
           self.typeline = typeline
           self.text = text
           self.power = power
           self.toughness = toughness
           self.types = types
           self.subtypes = subtypes

def transform_row_to_card(dfset0, row_number):
    cardname = dfset0.iloc[row_number]["name"]
    manaCost = dfset0.iloc[row_number]["manaCost"]
    cmc = dfset0.iloc[row_number]["cmc"]
    colorIdentity = dfset0.iloc[row_number]["colorIdentity"]
    # artist = dfset0.iloc[1]["artist"]
    typeline = dfset0.iloc[row_number]["type"]
    text=dfset0.iloc[row_number]["text"]
    power=dfset0.iloc[row_number]["power"]
    toughness=dfset0.iloc[row_number]["toughness"]
    types = dfset0.iloc[row_number]["types"]
    subtypes = dfset0.iloc[row_number]["subtypes"]
    testobject = card(cardname,manaCost,cmc,colorIdentity,typeline,text,power,toughness,types,subtypes)
    return testobject


root_dir = Path(__file__).parent.parent
path_to_decks = root_dir/"data"/"decks"
path_to_deck1 = path_to_decks/"deck1.csv"
path_to_deck2 = path_to_decks/"deck2.csv"
deck1=pd.read_csv(path_to_deck1)
deck2 = pd.read_csv(path_to_deck2)

deck1=[transform_row_to_card(deck1,i) for i in range(60)] # use iterrows()
hand1 = random.sample(deck1,7)
#begin game

for card in hand1:
    print(card.cardname)
redraw = input("Do you want a redraw? yes or no? ")
print(f"The player chose {redraw}")

if redraw == "yes":
    hand1 = random.sample(deck1, 7)
for card in hand1:
    print(card.cardname)

graveyard1=[]
graveyard2=[]
exilezone1=[]
exilezone2=[]

#hand1= sample deck1 of seven cards
# hand2= sample deck2 of seven cards
#
# random.shuffle() #shuffles a list in place,
#
# do you keep the hand y/n?












