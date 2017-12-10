from imgurpython import ImgurClient
import os
import random

# authentification for imgur  using environmental variables
client_id = os.environ.get('IMGUR_ID')
client_secret = os.environ.get('IMGUR_SECRET')
# set client object
client = ImgurClient(client_id, client_secret)

# function that takes all the pictures from the front page of imgur and adds to a list
def main(): 

	# commenting out my first function.

	#url_list = []
	#items = client.gallery()
	#i = 0
	#for item in items:
	#	url_list.append(item.link) 
	#	i = i + 1
	# takes a random url from the list and prints it out on the screen
	#print(random.choice(url_list))

	x = 'bird'

	print('•')


if __name__ == '__main__': 
	main()