# practicing ArgParse for command line/terminal interfaces
import argparse
import sys

def main(): 
	parser = argparse.ArgumentParser()


def calc(x, y, operation):  
	if operation == 'add': 
		return x + y
	elif operation == 'sub': 
		return x - y
	elif operation == 'mul': 
		return x * y
	elif operation == 'div': 
		return x / y

operation = calc(7, 3, 'div')
print (operation)
