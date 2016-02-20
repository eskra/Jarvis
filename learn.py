#!/usr/bin/python
import sys 
import json 

#this script helps jarvis learn information and stores it in his DB 

string = 'vocab.txt'
txt = open(string)
j = json.loads( txt.read() ) 

#check memory and see if he knows this word
def search_word(word):
	if word in j: 
		print( j[word][0]['0'] )
	else: 
		print("word does not exist in DB")

#learn vocab by adding it to its dictionary
# def learn(word):

while True:
	s = raw_input("what do you want to teach me? \n")
	search_word(s)
