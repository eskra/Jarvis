#!/usr/bin/python

def getString():
	f = open('output.txt', 'r')
	transcriptions = []
	words = []
	final_transcription = ""

	for line in f:
		if '\'transcriptions\':' in line:
			transcriptions = line.split('\'')
			final_transcription = transcriptions[3]

		if '\'words\':' in line:
			while not line.startswith("<<<<"):
				words.append(line)
				line = f.readline()

	return final_transcription

