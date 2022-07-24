
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




cardname = dfset0.iloc[1]["name"]       # equivalently dfset0.at[1,"name"]
manaCost = dfset0.iloc[1]["manaCost"]
cmc = dfset0.iloc[1]["cmc"]
colorIdentity = dfset0.iloc[1]["colorIdentity"]
# artist = dfset0.iloc[1]["artist"]
typeline = dfset0.iloc[1]["type"]
text=dfset0.iloc[1]["text"]
power=dfset0.iloc[1]["power"]
toughness=dfset0.iloc[1]["toughness"]
types = dfset0.iloc[1]["types"]
subtypes = dfset0.iloc[1]["subtypes"]


testobject = card(cardname,manaCost,cmc,colorIdentity,typeline,text,power,toughness,types,subtypes)


print(testobject.cardname)
print(testobject.manaCost)
print(testobject.cmc)
print(testobject.typeline)
print(testobject.colorIdentity)
print(testobject.text)
print(testobject.power)
print(testobject.toughness)
print(testobject.types)
print(testobject.subtypes)







