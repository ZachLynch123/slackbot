from bot import *
import os 
import requests
import logging
import os

class Bot(SlackBot): 
	def __init__(self,*args, **kwargs): 
		super().__init__(*args, **kwags)
		self.logger = logging.getLogger(__name__)

	@SlackCommand()
	def hello(context): 
		context.send("Hello Zach!")