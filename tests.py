from imgurpython import ImgurClient
import os

def main(): 
	# Practicing string concatination
	names = ['Jeff', 'Gary', 'Jill', 'Sam']
	location_of_files = '/Users/Zach/myenv/project_folder/slack_bot'
	file_name = 'requirements.txt'
	# not the right way to go about this
	print(location_of_files + '/' + file_name)
	with open(os.path.join(location_of_files, file_name)) as f:
		print (f.read())

	#for name in names: 
		# print('hello there, ' + name)
	#	print(' '.join(['Hello there', name]))
	# if you don't know how join works, it's not readable
	# but it's more efficient, if you're going to concatinate 2 or more strings, use join. It will scale better and use less processing
	print(', '.join(names))

if __name__ == "__main__": 
	main()
