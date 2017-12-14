from imgurpython import ImgurClient
import os

client_id = os.environ.get('IMGUR_ID')
client_secret = os.environ.get('IMGUR_SECRET')

client = ImgurClient(client_id, client_secret)

items = client.gallery()

xyz = [i for i in range(5)]
print(xyz)
zxy = (i for i in range(5))
print(zxy)
for i in zxy:
	print(i)



