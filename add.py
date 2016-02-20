#!/usr/bin/python
import sys 
import json 

string = 'data.txt'
txt = open(string)
j = json.loads( txt.read() ) 

a_dict = {"name" : "Tommy"}

j.update(a_dict)

with open(string, 'w') as f:
	json.dump(j,f)