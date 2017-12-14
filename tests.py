from imgurpython import ImgurClient
import os

def main(): 
	# Practicing string concatination
	names = ['Jeff', 'Gary', 'Jill', 'Sam']

	#for name in names: 
		# print('hello there, ' + name)
	#	print(' '.join(['Hello there', name]))
	# if you don't know how join works, it's not readable
	# but it's more efficient, if you're going to concatinate 2 or more strings, use join. It will scale better and use less processing
	
	print(', '.join(names))

if __name__ == "__main__": 
	main()
