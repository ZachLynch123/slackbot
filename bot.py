import time
import os
import threading
import logging
import urllib.request
from slackclient import SlackClient
import pdb

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
	# This class will also handle all commands sent to the bot using the decorator created above
	def __init__(self, token, prefix = "!"): 
		super().__init__(token)
		pdb.set_trace()
		self.prefix = prefix
		self.read_incoming_thread = threading.Thread(target=self.read_messages)
		self.events = {"message": self.on_message
		}
		self.__logger = logging.getLogger(__name__)
	def read_messages(self): 
		pdb.set_trace()
		# Continuously recieve new messages
		
		if self.rtm_connect(): 
			while True:
				self.parse_output(self.rtm_read()) # Get messages from output while bot is connected to the channel
				time.sleep(1)
			while False: 
				self.parse_output("...")

	def send_message(self,channel,content): 
		# Post message to the channel
		# Args = channel -- slack thannel ID 
		# content -- the message text to send

		resp = self.api_call("chat.postMessage", channel=channel, text=content, as_user=True)
		self.__logger.debug("Sent a message to {}: {}".format(channel, content))
		return resp.get("channel"), resp.get("ts")

	def rtm_send(self, content):
		requests.post()

	def parse_output(self, output_list): 
		# pase the output of self.rtm_read() method
		# args = output_list -- the response from self.rtm_read()

		if output_list: 
			for output in output_list: 
				if event_function: 
					event_function(**output)
				self.__logger.debug(output)

	def get_command(self, command_name): 
		c = {"name": command_name, "callback": SlackCommand.commands.get(command_name)}
		return c

	def get_usage(self, command):
		args_spec = inspect.getargspec(command.get("callback"))  # Get arguments of command
		args_info = []
		[args_info.append("".join(["<", arg, ">"])) for arg in args_spec.args[1:]]  # List arguments
		if args_spec.defaults is not None:
			for index, default in enumerate(args_spec.defaults):  # Modify <> to [] for optional arguments
				default_arg = list(args_info[-(index + 1)])
				default_arg[0] = "["
				default_arg[-1] = "]"
				args_info[-(index + 1)] = "".join(default_arg)
		if args_spec.varargs:  # Compensate for *args
			args_info.append("<" + args_spec.varargs + ">")
			args_info.insert(0, self.prefix + command.get("name"))  # Add command name to the front
		return " ".join(args_info)  # Return args

	def on_message(self, **message):
		# This function is ran every time a message is sent, whether or not it's directed to ankha or not
		user = self.api_call("users.info", user=message.get("user")).get("user")
		channel = self.api_call("channels.info", channel=message.get("channel"))
		if user and channel.get("channel") and message.get("text"):
			self.__logger.info("({}){}: {}".format(channel.get("channel").get("name"),
				user.get("profile").get("display_name"), message.get("text")))

		if message.get("text"): 
			if message.get("text").startswith(self.prefix): 
				message["args"] = message.get("text").split()
				self.on_command(message)

	def on_ready(self, **output): 
		# Function is when the bot is ready to and reading messages
		self.__logger.info(output.get("type"))

	def on_command(self, command): 
		# Function is ran whenever a command is directed to the bot

		cmd = command.get("args")[0][len(self.prefix):] # take the command prefix out of the command
		args = command.get("args")[1:]
		if cmd in SlackCommand.commands:  # Checks if the command is valid
			cntxt = Context(self, command)
			cmd_function = SlackCommand.commands.get(cmd)
			cntxt.command["callback"] = cmd_function
			cntxt.command["name"] = cmd
			cntxt.command_name = cmd
			try:
				cmd_function(cntxt, *args)
			except TypeError: 
				cntxt.send("Not a valid command. Type `do` to see a list of commands")

