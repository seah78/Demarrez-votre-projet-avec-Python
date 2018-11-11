# -*-coding: utf8 -*-

quotes = [
	"Ecoutez-moi, monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !",
	"On doit pouvoir choisir entre s'écouter parler et se faire entendre."

]

characters = [
	"Alvin et les Chipmunks",
	"Babar",
	"Betty Boop",
	"Calimero",
	"Casper",
	"Le chat potté",
	"Kirikou"
]

user_answer = input("Tapez entrée pour connaître une autre citation ou B pour quitter le programme.")
# Show random quote


# If user_ansmwer == "B":

if user_answer == "B":
		
	# leave the program
	pass

# Else:
elif user_answer == "C":
	print("C pas la bonne réponse ! Et G pas d'humour, je c...")
	
else:
	
	# show another quote

	def show_random_quote(my_list):
		# get a random number	
		item = my_list[0]
		
		# get a quote from an array
		return item

	print(show_random_quote(quotes))
	
	