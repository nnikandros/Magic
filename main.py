import random

import pandas as pd



dfset0 = pd.read_csv("set0.csv")





class card:
       def __init__(self, cardname,manaCost,cmc,colorIdentity ,typeline,text, power,toughness,types,subtypes): # , artist,, ,, rarity): #, ):
           self.cardname = cardname
           self.manaCost = manaCost
           self.cmc = cmc
           self.colorIdentity = colorIdentity
           # self.artist = artist
           self.typeline = typeline
           self.text = text
           self.power = power
           self.toughness = toughness
           # self.rarity=rarity
           self.types = types
           self.subtypes = subtypes
              # self.flavor = flavor
            # self.layout = layout
             #self.multiverseid = multiverseid
           #self.printings = printings



def transform_row_to_card(dfset0, row_number):
    cardname = dfset0.iloc[row_number]["name"]       # equivalently dfset0.at[1,"name"]
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

transform_row_to_card(dfset0,0)
print(transform_row_to_card(dfset0,0))
print(transform_row_to_card(dfset0,0).manaCost)

# deck1= [transform_row_to_card(dfset0,0), transform_row_to_card(dfset0,1)]

deck1=[transform_row_to_card(dfset0,i) for i in range(60)]

print(deck1[3].cardname)

deck2=[transform_row_to_card(dfset0,i) for i in range(60,120)]

print(deck2[5].typeline)

hand1 = random.sample(deck1,7)

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
#hand2= sample deck2 of seven cards

# do you keep the nad y/n?


# print(testobject.cardname)
# print(testobject.manaCost)
# print(testobject.cmc)
# print(testobject.typeline)
# print(testobject.colorIdentity)
# print(testobject.text)
# print(testobject.power)
# print(testobject.toughness)
# print(testobject.types)
# print(testobject.subtypes)









