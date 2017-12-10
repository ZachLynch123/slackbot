from imgurpython import ImgurClient
import os

client_id = os.environ.get('IMGUR_ID')
client_secret = os.environ.get('IMGUR_SECRET')
client  = ImgurClient(client_id, client_secret)

def main(): 
	q = 'birds'
	items = client.gallery_search(q, advanced=None, sort='time', window='all', page=0)
	for item in items: 
		print (items)

if __name__ == "__main__": 
	main()
