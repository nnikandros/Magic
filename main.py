import pandas as pd
dfset0 = pd.read_csv("set0.csv")





class card:
       def __init__(self, name,  manaCost ): # , cmc, colorIdentity, artist, number, type,
     #   text, printings, flavor, layout, multiverseid, power,toughness, rarity, subtypes, types):
           self.name = name
           self.manaCost =manaCost
            # self.cmc = cmc
            # self.colorIdentity = colorIdentity
            # self.artist = artist
            # self.number = number
            # self.type = type
            # self.text = text
            # self.printings = printings
            # self.flavor = flavor
            # self.layout = layout
            # self.multiverseid = multiverseid
            # self.power = power
            # self.toughness = toughness
            # self.rarity=rarity
            # self.subtypes=subtypes
            # self.types=types




name=dfset0.iloc[1]["name"] # same as dfset0[1].name
manaCost=dfset0.iloc[1].manaCost
testobject=card(name,manaCost)
print(testobject.name)
print(testobject.manaCost)






