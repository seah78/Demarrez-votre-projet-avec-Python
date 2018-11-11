# -*-coding: utf8 -*-
import random

quotes = [
	"Ecoutez-moi, monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !",
	"On doit pouvoir choisir entre s'écouter parler et se faire entendre."

]

characters = [
	"alvin et les Chipmunks",
	"Babar",
	"betty Boop",
	"calimero",
	"casper",
	"ce chat potté",
	"Kirikou"
]

def show_random_item(my_list):
	rand_numb = random.randint(0, len(my_list)-1)	#radom number
	item = my_list[rand_numb]								# get a quote from a list
	return item													#return the item
	
def message(character,quote):
	n_character = character.capitalize()
	n_quote = quote.capitalize()
	return "{} a dit : {}".format(n_character, n_quote)
	
user_answer = input("Tapez entrée pour connaître une citation ou B pour quitter le programme : ")

while user_answer != "B":
	print(message(show_random_item(characters), show_random_item(quotes)))
	user_answer = input("Tapez entrée pour connaître une autre citation ou B pour quitter le programme : ")
	
	