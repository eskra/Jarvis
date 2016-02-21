import sys 
import json 
import os 
import dictionary
import get_intent
import parseOutput
import user
import appscript

def mainFunc():
	string = parseOutput.getString()
	result = get_intent.nlu(string)
	if result[0] == "user":
		greeting = user.validate_user(result[1])
		print(greeting[0])
	if result[0] == "addDefinition":
		dictionary.addDefinition(result[1], result[2])
	if result[0] == "getDefinition":
		dictionary.getDefinition(result[1])
	#if result[0] == 

mainFunc()