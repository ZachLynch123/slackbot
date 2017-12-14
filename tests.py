from imgurpython import ImgurClient
import os

def main(): 
	# Practicing string concatination
	names = ['Jeff', 'Gary', 'Jill', 'Sam']

	for name in names: 
		# print('hello there, ' + name)
		print(' '.join(['Hello there', name]))

if __name__ == "__main__": 
	main()
