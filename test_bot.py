from bot import *
import os 
import requests
import logging
import os

class Bot(SlackBot): 
	def __init__(self,*args, **kwargs): 
		token = os.environ.get('SLACK_BOT_TOKEN')
		super().__init__(*args, **kwargs)
		self.logger = logging.getLogger(__name__)

	@SlackCommand()
	def hello(context): 
		context.send("Hello Zach!")

if __name__ == "__main__": 
	print("CRUSADER ONLINE")
	pdb.set_trace()
	Bot().__init__()