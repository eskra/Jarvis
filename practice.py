import sys 
import json 

#use input() to evaluate the user input, and the raw input takes the string value rawly
# string = raw_input("please enter your file name: ")
string = 'data.txt'
txt = open(string)
j = json.loads( txt.read() ) 

def readLine(line):
	for word in line.split():
		if word in j: 
			return word 
		else: 
			continue
	return "error"

while True:
	string = raw_input("hi Tommy, what do you want to know about me? \n")
	if readLine(string) == "error":
		print("you don't make any sense... \n")
	else:
		print j[ readLine(string) ] 
		print ("\n")
