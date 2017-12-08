from json import JSONEncoder

class MyEnconder(JSONEncoder): 
	def default(self, o): 
		return o.__dict__
