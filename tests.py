from imgurpython import ImgurClient
import os

client_id = '71f3976ee48114b'
client_secret = os.environ.get('secret')

client = ImgurClient(client_id, client_secret)

def main(): 
	print('test 1 2 ')

if __name__ == '__main__': 
	main()