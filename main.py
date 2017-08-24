class Main:

	rand_seed = 0
	while True:
		try:
			rand_seed = int(input("Private Key: "))
			break
		except TypeError:
			print("That's not an integer, try again.")
	raw_message = input("Message here: ")
	
	def get_message():
		return raw_message
