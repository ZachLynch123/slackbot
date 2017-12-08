import os
import time
from slackclient import SlackClient
from weather import Weather
weather = Weather()
# starterbot's ID as an environment variable
BOT_ID = os.environ.get("BOT_ID")

# constants 
AT_BOT = "<@" + BOT_ID + ">"

EXAMPLE_COMMAND = "do"
# instantiate Slack & Twilio clients

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
# remember to watch kill will's tuturial to get some info on how to impliment different functions
# video starts at 1:08:13
def weather(command,channel): 
	location = weather.lookup_by_location()
	condition = location.condition()
	
	forecasts = location.forecast()
	for forecast in forecasts:
	    print(forecast.text())
	    print(forecast.date())
	    print(forecast.high())
	    print(forecast.low())


# learn how to get the weather command into the handle command 
def handle_command(command,channel): 
	# receives commands directed at the bot and determines if they are valid
	# commands or not. If so, then act on the command. If not, return 
	# what the bot needs for clarification
	response = "Not sure what you mean. Use the `do` command to see what awesome things I can do!"
	# check if the response starts with the example command
	if command.startswith(EXAMPLE_COMMAND): 
		response = "Well.. I can't really do anything right now, but I'll be able to do some cool stuff soon!"
	if command.startswith("ditto"): 
		message = command[6:]
		response = message
	if command.startswith("forecast"): 
		location = command[8:]
		forecasts = location.forecast()
		for forecast in forceasts: 
			print(forecast.text())
			print(forecast.date())
			print(forecast.high())
			print(forceast.low())


	slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)




def parse_slack_output(slack_messages): 
	# Slack's 'Real Time Messaging'(rtm) API is an event firehose. (look up fire hose later)
	# this parsing function returns None unless a message is directed at the Bot based on its ID

	if slack_messages and len(slack_messages) > 0: 
		for message in slack_messages: 
			if message and 'text' in message and AT_BOT in message['text']: 
				command = message['text'].split(AT_BOT)[1].strip().lower()
				channel = message['channel']
				# return text after the @ mention, whitespace removed.
				return command, channel
	return None, None

# going to follow raveN's lead and make a weather function using a weather api


# fixed code can't seem to fgure out how to put my own outputs in

# Online and ready! 
if __name__ == "__main__": 
	READ_WBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
	if slack_client.rtm_connect(): 
		print("CRUSADER, ONLINE!")
		while True: 
			command, channel = parse_slack_output(slack_client.rtm_read())
			if command and channel: 
				handle_command(command, channel)
				time.sleep(READ_WBSOCKET_DELAY)
	else: 
		print("Connection failed. Invalid Slack token or bot ID?")



