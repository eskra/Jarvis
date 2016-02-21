#!/usr/bin/python
import json

def initialize():
	f = open("dictionary.json", "r")
	data = json.load(f)
	new_data = dict()
	for i in data.keys():
		new_data[str(i)] = str(data[i])
	f.close()
	return new_data

def addDefinition(word, definition):
	data = initialize()
	data[word] = definition
	f = open("dictionary.json", "w")
	f.write(str(data))
	f.close()

def getDefinition(word):
	data = initialize()
	if word in data.keys():
		print(data[word])
	else:
		print("I don't know what that means.\nCan you give me the definition in a full sentence?")

