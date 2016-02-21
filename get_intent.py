import sys 
import json 
import os 

#ajwad wants just a username like tommy or esther
#preference variable travel, diet, movie, music. recognize one of these 4 words, 
#these variables tell us where to parse the next varialbe
#i like the music arctic monkey 
#preference analysid
# knowledge base like "do you know math" or do you know some function 
# user_in = esther's program 

# def findName(line):
# 	if line[0:19] == "you are speaking to":
# 		return line[20:40]
# 	else: 
# 		return "e1"

# string will be the user input coming from the asr done by esther
keywords = {"travel","diet","movie","music"}
introduction = {"you are speaking to","i am","i'm"}

def nlu(string):
	# users
	for intro in introduction:
		if intro in string.lower():
			return ("user.py", string.lower().split(intro)[-1].lstrip(" "))
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
		return ("getDefinition", word)


