import time
import os
import threading
import logging
import urllib.request
from slackclient import SlackClient

# Reference raveN's code to creae decorators
# Keyword arguments: Name --the name of the command (default None)
class SlackCommand:
	commands = {}
	def __init__(self, name=None): 
		self.name = name

	def __call__(self, f): 
		if self.name is None: 
			self.name = f.__name__
			self.commands[self.name] = f
		return f

class Context: 
	# Get the context of the command
	# Arguments bot -- The actual Slack bot
	# Command -- the users inputted command

	def __init__(self, bot, command): 
		self.bot = bot
		self.command = command
		self.command_name = None
		self.callback = None

	def send(self, content): 
		return self.bot.send_message(channel=self.command.get("channel"), content=content)

class SlackBot(SlackClient): 
	# Initialize the slackbot Ankha
	# Arguments: token -- bot's token
	# Keyword Arguments -- Prefix -- The bot's command prefix (lets default it to /)
	def __init__(self, token, prefix = "/"): 
		token = os.environ.get("SLACK_BOT_TOKEN")
		super().__init__(token)
		self.prefix = prefix
		self.read_incoming_thread = threading.Thread(target=self.read_messages)
		self.events = {"message": self.on_message
		}
		self.__logger = logging.getLogger(__name__)

	def send_message(self,channel,content): 
		# Post message to the channel
		# Args = channel -- slack thannel ID 
		# content -- the message text to send

		resp = self.api_call("chat.postMessage", channel=channel, text=content, as_user=True)
		self.__logger.debug("Sent a message to {}: {}".format(channel, content))
		return resp.get("channel"), resp.get("ts")

	def rtm_send(self, content):
		requests.post()


















