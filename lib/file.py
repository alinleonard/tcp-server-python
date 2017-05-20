#!/usr/bin/env python

history_path = '/history/history.txt'

def write(text):
	history = open(history_path, 'w')
	history.write(text)
	history.close()

	