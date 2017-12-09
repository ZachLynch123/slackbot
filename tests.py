from imgurpython import ImgurClient
import os

client_id = os.environ.get('IMGUR_ID')
client_secret = os.environ.get('IMGUR_SECRET')
print(client_secret)

client = ImgurClient(client_id, client_secret)

def main(): 
	items = client.gallery()
	for item in items: 
		print(item.link)

if __name__ == '__main__': 
	main()