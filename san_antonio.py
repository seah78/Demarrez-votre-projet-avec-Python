# -*-coding: utf8 -*-

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

def show_random_quote(my_list):
	# TODO : get a random number	
	item = my_list[0]
	# get a quote from an array
	return item

user_answer = input("Tapez entrée pour connaître une autre citation ou B pour quitter le programme.")

while user_answer != "B":
	print(show_random_quote(quotes))
	user_answer = input("Tapez entrée pour connaître une autre citation ou B pour quitter le programme.")	

for character in characters:
	n_character = character.capitalize()
	print(n_character)


	print(show_random_quote(quotes))
	
	