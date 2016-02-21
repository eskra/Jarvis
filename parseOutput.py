#!/usr/bin/python

def getString():
	f = open('output.txt', 'r')
	transcriptions = []
	words = []
	final_transcription = ""

	for line in f:
		if '\'transcriptions\':' in line:
		#if line.startswith('\'transcriptions\':'):
			transcriptions = line.split('\'')
			final_transcription = transcriptions[-2]

		if '\'words\':' in line:
		#if line.startswith('\'words\':'):
			while not line.startswith("<<<<"):
				words.append(line)
				line = f.readline()

	return final_transcription
	# print(final_transcription)
	# print(words)
