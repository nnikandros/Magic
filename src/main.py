import random
import pandas as pd
from pathlib import Path


class Card:
    def __init__(self, card_name, mana_cost, cmc, color_identity, type_line, text, types,subtypes, tapped_status=""): # , artist,, ,, rarity): #, ):
        self.card_name = card_name
        self.mana_cost = mana_cost
        self.cmc = cmc
        self.color_identity = color_identity
        self.type_line = type_line
        self.text = text
        self.types = types
        self.subtypes = subtypes
        self.tapped_status = tapped_status
        self.total = card_name, mana_cost, type_line, text

    def display(self):
        print(self.total)


    def tap(self):
        self.tapped_status = "tapped"

    def untap(self):
        self.tapped_status = "untapped"

    def cast(self):
        pass


class Creature(Card):
    def __init__(self, card_name, mana_cost, cmc, color_identity, type_line, text,types, subtypes, tapped_status, power, toughness):
        Card.__init__(self, power, toughness)
        self.power = power
        self.toughness = toughness
        self.total = card_name, mana_cost, type_line, text, power, toughness

    def display(self):
        print(self.total)


class Planeswalker(Card):
    def __init__(self, card_name, mana_cost, cmc, color_identity, type_line,text,types,subtypes, tapped_status, loyalty):
        Card.__init__(self, loyalty)
        self.loyalty = loyalty
        self.total = card_name, mana_cost, type_line, text, loyalty

    def up_tick(self):
        self.loyalty += 1

    def down_tick(self):
        self.loyalty -= 1

    def display(self):
        print(self.total)

class Enchantment(Card):
    pass


class Artifact(Card):
    pass


class Deck(list):

    def shuffle(self):
        return random.shuffle(self)

    def draw(self, lst):
        card = self.pop()
        return lst.append(card)  # lst.append(self.pop())


class Hand(list):
    def discard(self, nameofcard):
        pass


class Stack(list):
    pass



#
#
# def transform_row_to_card(dfset0, row_number):
#     cardname = dfset0.iloc[row_number]["name"]
#     manaCost = dfset0.iloc[row_number]["manaCost"]
#     cmc = dfset0.iloc[row_number]["cmc"]
#     colorIdentity = dfset0.iloc[row_number]["colorIdentity"]
#     # artist = dfset0.iloc[1]["artist"]
#     typeline = dfset0.iloc[row_number]["type"]
#     text=dfset0.iloc[row_number]["text"]
#     power=dfset0.iloc[row_number]["power"]
#     toughness=dfset0.iloc[row_number]["toughness"]
#     types = dfset0.iloc[row_number]["types"]
#     subtypes = dfset0.iloc[row_number]["subtypes"]
#     testobject = card(cardname,manaCost,cmc,colorIdentity,typeline,text,power,toughness,types,subtypes)
#     return testobject
#
#
# root_dir = Path(__file__).parent.parent
# path_to_decks = root_dir/"data"/"decks"
# path_to_deck1 = path_to_decks/"deck1.csv"
# path_to_deck2 = path_to_decks/"deck2.csv"
# deck1=pd.read_csv(path_to_deck1)
# deck2 = pd.read_csv(path_to_deck2)
#
# deck1 = [transform_row_to_card(deck1,i) for i in range(60)] # use iterrows()

# deck2 =

player1 = input("Please give name of the first player:")
player2 = input("Please give name of the second player:")
players = [player1, player2]  #to be used for cycle itertools
choice = input("To determine which player takes the first turn, please choose Heads or Tails:")
print(f"Player chose {choice}")
result = random.choice(["Heads", "Tails"])
print(f"The result of the coin toss was {result}")
if choice == result:
    print(f"{player1} goes first!")
else:
    print(f"{player2} goes first! ")  # to fix



# #begin game
print(f"Each player will now draw 7 cards and decide if they want a mulligan")
## hand1 = [deck1.pop() for _ in range(7)]
# #hand2 = [deck2.pop() for _ in range(7)]
# graveyard1=[]
# graveyard2=[]
# exilezone1=[]
# exilezone2=[]

# for card in hand1:
#     print(card.cardname)
# redraw = input("Do you want a redraw? yes or no?")
# print(f"The player chose {redraw}")
#
# if redraw == "yes":
#     hand1 = random.sample(deck1, 7)
# for card in hand1:
#     print(card.cardname)
#
# graveyard1=[]
# graveyard2=[]
# exilezone1=[]
# exilezone2=[]
#
# #hand1= sample deck1 of seven cards
# # hand2= sample deck2 of seven cards
# #
# # random.shuffle() #shuffles a list in place,
# #
# # do you keep the hand y/n?












