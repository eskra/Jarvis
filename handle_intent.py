import sys 
import json 
import os 
import dictionary
import get_intent
import parseOutput

while True:
	#string = parseOutput.getString()
	string = raw_input("please enter your input \n")
	result = get_intent.nlu(string)
	if result[0] == "user.py":
		# 
	if result[0] == "addDefinition":
		definition.addDefinition(result[1], result[2])
	if result[0] == "getDefinition":
		definition.getDefinition(result[1])
	if result[0] == "preferenceAnalysis.py"
		# blah blah need ajwad's help 
	
