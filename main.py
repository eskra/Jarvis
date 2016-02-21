import sys 
import json 
import os 

#use input() to evaluate the user input, and the raw input takes the string value rawly
# string = raw_input("please enter your file name: ")
string = 'data.txt'
txt = open(string)
j = json.loads( txt.read() ) 

def goto(linenum):
	global line
	line = linenum

# def findName(line):
# 	if line[0:19] == "you are speaking to":
# 		return line[20:40]
# 	else: 
# 		return "e1"

def readLine(line):
	for word in line.split():
		if word in j: 
			return word 
		else: 
			continue
	return "error"

while True:
	string = raw_input("hi Tommy, what do you want to know about me? \n")
	# if findName(string) != "e1":
	# 	print "hello " + findName(string)
	if readLine(string) == "error":
		print("you don't make any sense... \n")
	else:
		print j[ readLine(string) ] 
		print ("\n")
