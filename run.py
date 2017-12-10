import test_bot
import logging
import os

def main(): 
	logging.basicConfig(level=logging.INFO)
	test_bot.Bot(os.environ.get("SLACK_BOT_TOKEN"))
if __name__ =="__main__": 
	main()