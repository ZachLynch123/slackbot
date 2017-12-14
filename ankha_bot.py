from Slack.Slack import SlackBot, SlackCommand
import requests
import logging
import os
import random
from imgurpython import ImgurClient

client_id = os.environ.get('IMGUR_ID')
client_secret = os.environ.get('IMGUR_SECRET')
client  = ImgurClient(client_id, client_secret)

class Bot(SlackBot): 
	def __init__(self,*args, **kwargs): 
		super().__init__(*args, **kwargs)
		self.logger = logging.getLogger(__name__)

	@SlackCommand()
	def help(context): 
		context.send("Here's a list of commands: \n •`random` \n •`search <search query> \n •`help_django` \n •`help flask`")
	@SlackCommand()
	def random(context):
		url_list = []
		items = client.gallery()
		i = 0
		for item in items:
			url_list.append(item.link) 
			i = i + 1
		context.send(random.choice(url_list))

	@SlackCommand()
	def help_django(context): 
		context.send("You need help with Django? dragon_lu recommended https://simpleisbetterthancomplex.com/series/beginners-guide/1.11/ \n \
			Soon Kill.Will is going to have his own tutorial up, and I'll post that when it happens \n Hope this helps in the mean time!!")

	@SlackCommand()
	def help_flask(context): 
		context.send("You need help with flask? I recommend checking out https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world-legacy \ \n Starting from part one, I'm sure this will have everything you'll need.")

	@SlackCommand()
	def search(context, *area): 
		# Impliment a search function to search imgur for pictures
		q = " ".join(area) # Gets the search query after the prefix
		url_list = []
		items = client.gallery_search(q) # Searches Imgur for all the items with the query
		i = 0
		for item in items: 
			url_list.append(item.link)
			i = i + 1
		context.send(random.choice(url_list))







		