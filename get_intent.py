import sys 
import json 
import os 
import parseOutput
import appscript


keywords = {"travel","diet","movie","music"}
introduction = {"you are speaking to","i am","i'm","my name is"}

def nlu(string):
	# users
	for intro in introduction:
		if intro in string.lower():
			return ("user", string.lower().split(intro)[-1].lstrip(" "))
	# preferences
	for key in keywords:
		if key in string.lower():
			return key
	# tasks
	if "do you know" in string:
		return string.lower().split("do you know")[-1].lstrip(" ")
	# add definition
	if "means" in string.lower(): 
		data = string.lower().split("means")
		word = data[0].lstrip(" ")
		definition = data[-1].lstrip(" ")
		return ("addDefinition", word, definition)
	# get definition
	if "mean" in string.lower():
		data = string.lower().split(" ")
		word = data[-2]
		print("getDefinition", word)
		return ("getDefinition", word)



