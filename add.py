#!/usr/bin/python
import sys 
import json 

string = 'data.txt'
txt = open(string)
j = json.loads( txt.read() ) 

# a_dict = {"esther" : "chubs"}

# j.update(a_dict)

with open(string, 'w') as f:
	json.dump(j,f)

while True: 
	word = raw_input("what is the word? \n")
	definition = raw_input("what is the definition? \n")
	print(word)
	print(definition)
	a_dict = '{ "%s" : "%s" }' % (str(word), str(definition))
	j.update(a_dict)