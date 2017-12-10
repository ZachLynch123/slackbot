import time
import event
import os
from slackclient import SlackClient

class Bot(object): 
	def __init__(self): 
		self.slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
		self.bot_name = "ankha"
		self.bot_id = os.environ.get('BOT_ID')

	if self.bot_id = None: 
		exit("Error! Could not find " + self.bot_name)

	self.event = event.Event(self)
	self.listen()

	def listen(self): 
		if self.slack_client.rtm_connect(with_team_state=False): 
			print('CRUSADER ONLINE')
			while True: 
				self.event.wait_for_event()

				time.sleep(1)
		else: 
			exit("ERROR! Connection failed")