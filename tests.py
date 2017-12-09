from imgurpython import ImgurClient
import os

client_id = os.environ.get('IMGUR_ID')
client_secret = os.environ.get('IMGUR_SECRET')
print(client_secret)

client = ImgurClient(client_id, client_secret)

def main(): 
	url_list = []
	items = client.gallery()
	i = 0
	for item in items:
		url_list.append(item.link) 
		print(url_list[i])
		i = i + 1

if __name__ == '__main__': 
	main()