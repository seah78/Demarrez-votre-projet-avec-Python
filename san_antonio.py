# -*-coding: utf8 -*-
import random
import json

# Give a json file and return a list
def read_values_from_json(path, nkey):
	values = []
	with open(path) as f:
		data = json.load(f)
		for entry in data:
			values.append(entry[nkey])
	return values

# Give a json and return a list
def clean_strings(sentences):
	cleaned = []
	# Strore quotes on a list. Create an empty list and add each sentence one by one.
	for sentence in sentences:
		# Clean quotes from whitespaces and so on
		clean_sentence = sentence.strip()
		# don't use extend as it adds each letter one by one !
		cleaned.append(clean_sentence)
	return cleaned

# Return a random item in a list
def get_random_item_in(my_list):
	rand_numb = random.randint(0, len(my_list)-1)
	item = my_list[rand_numb]	
	return item

# Return a random value from a json file
def get_random_item (source_path, xkey):
	all_values = read_values_from_json(source_path, xkey)
	clean_values = clean_strings(all_values)
	return get_random_item_in(all_values)

# Print a random sentence.
def print_random_sentence():
	rand_quote = get_random_item('quotes.json', 'quote')
	rand_character = get_random_item('characters.json', 'character')
	print(">>>> {} a dit : {}".format(rand_character, rand_quote))

#Programm	
def main_loop():
	while True:
		print_random_sentence()
		message = ('Voulez-vous voir une autre citation ?'
						'Pour sortir du programme, tapes [B].')
		choice = input(message).upper()
		if choice == 'B':
			break
			# this will stop the loop !

if __name__ == '__main__':
	main_loop()
	