#!/usr/bin/python
import json

while True:
	f = open('data.txt', 'r')

	# decode the file
	data = json.loads(f.read().replace("\'",'"'))
		
	user_input_word = raw_input("Hi, what word would you like to know about?")
	if user_input_word in data.keys():
		print data[user_input_word]
		continue

	user_input_definition = raw_input("I don't know that word. Can you define it?")
	data[user_input_word] = user_input_definition

	new_data = {}
	for i in data.keys():
		new_data[str(i)] = str(data[i])

	f.close()
	f = open('data.txt', 'w')
	f.write(str(new_data))
	f.close()



