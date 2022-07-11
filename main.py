import pandas as pd

#hello Nikitas I'm a change, you can see that your local repo is now behind by one commit by "git status", and with "git pull" you'll get the commit locally

from pprint import pprint
import json

class card:
     def __init__(self, name, mana_cost, power,toughness,colour, cardtype, creaturetype, oracle):
            self.name = name
            self.mana_cost =mana_cost
            self.power=power
            self.toughness = toughness
            self.colour=colour
            self.cardtype=cardtype
            self.creaturetype=creaturetype
            self.oracle=oracle

Vadrik=card("Vadrik, Astral Archmage", 3, 1, 2, "RU","Legenrary Creature", "Human Wizard", "If it’s neither day nor night, it becomes day as Vadrik, Astral Archmage enters the battlefield. Instant and sorcery spells you cast cost {X} less to cast, where X is Vadrik’s power.Whenever day becomes night or night becomes day, put a +1/+1 counter on Vadrik"  )
# #print(Vadrik.name)
#
# #print(Vadrik.oracle)
#
# class player:
#         def __init__(self,name, healthpoints):
#                 self.name=name
#                 self.healthpoints=healthpoints
#         # def addhealthpoints(self):
#         #         self.healthpoints=self.healthpoints+1
#         def addhealthpoints(self,number):
#                 self.healthpoints=self.healthpoints+ number
#
# # class hand:
# #     def __init__(self, number,size ):
# #         self.number=number
# #         self.size=size
#
#
#
#
#
#
#
#
#
#
#
#
#
# Nikitas=player("Nikitas", 20)
#
#
# Nikitas.addhealthpoints(5)
# print(Nikitas.healthpoints)
# print(type(Nikitas.healthpoints))
# # print("Nikitas health points are :"); print(Nikitas.healthpoints)
#
# # Nikitas.addhealthpoints()
# # print(Nikitas.healthpoints)
# #print(Nikitas.addhealthpoints())
# # Alexander=player("Alexander",20)
#
# print(Nikitas.healthpoints)
# print(Alexander.name) ; print(Alexander.healthpoints)



# class Person:
#  def __init__(self, name, age):
#      self.name = name
#      self.age = age
#
# Nikitas=Person("Nikitas", 36)
# Nikitas.name
# print(Nikitas.name)
# print(Nikitas.age)

#df=pd.read_json("Azorius_GK2.json")

 #print(df)
# f = open("Azorius_GK2.json")
# json_file = json.load(f)
# data = json.load("Azorius_GK2.json")

df=pd.read_csv("cards.csv")
# print(df)

# print(df.iloc[:,3])
# print(df.columns)
# print(df['colors'])

print(df.columns)
# print((df.iloc[:5]).to_str())

# Vadrik=card("Vadrik, Astral Archmage", 3, 1, 2, "RU","Legenrary Creature", "Human Wizard", "If it’s neither day nor night, it becomes day as Vadrik, Astral Archmage enters the battlefield. Instant and sorcery spells you cast cost {X} less to cast, where X is Vadrik’s power.Whenever day becomes night or night becomes day, put a +1/+1 counter on Vadrik"  )

# rownumber=4
# row=df.iloc[4]
# print(row)
# color=df.loc[rownumber,"colors"]
# print(color)
# print(df.availability)
# print(df.colorIdentity)

# print(df.cardsphereId)
# df.drop("availability", 'boosterTypes','borderColor', 'cardKingdomEtchedId', 'cardKingdomFoilId',
# 'cardKingdomId', 'cardParts'   , 'cardsphereId','edhrecRank' ,   axis=1)