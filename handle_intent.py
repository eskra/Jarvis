import sys 
import json 
import os 
import dictionary
import get_intent
import parseOutput

while True:
	string = parseOutput.getString()
	# string = raw_input("please enter your input \n")
	print( get_intent.nlu(string) )
