from Slack.Slack import SlackBot, SlackCommand
import requests
import logging
import os
class Bot(SlackBot): 
	def __init__(self,*args, **kwargs): 
		super().__init__(*args, **kwargs)
		self.logger = logging.getLogger(__name__)

	@SlackCommand()
	
	def hello(context): 
		context.send("Hello Zach!")
	@SlackCommand()

	def random(context): 
		context.send("what")