# -*-coding: utf8 -*-
import random
import json

def read_values_from_json(nfile, nkey):
	values = []
	with open(nfile) as f:
		data = json.load(f)
		for entry in data:
			values.append(entry[nkey])
	return values

def message(character,quote):
	n_character = character.capitalize()
	n_quote = quote.capitalize()
	return "{} a dit : {}".format(n_character, n_quote)

def get_random_item_in(my_list):
	rand_numb = random.randint(0, len(my_list)-1)	#radom number
	item = my_list[rand_numb]								# get a quote from a list
	return item													#return the item

def get_random_item (xfile, xkey):
	all_values = read_values_from_json(xfile, xkey)
	return get_random_item_in(all_values)
	
#Programm	
user_answer = input("Tapez entrée pour connaître une citation ou B pour quitter le programme : ")

while user_answer != "B":
	print(message(get_random_item('characters.json', 'character'), get_random_item('quotes.json', 'quote')))
	user_answer = input("Tapez entrée pour connaître une autre citation ou B pour quitter le programme : ")
	
	