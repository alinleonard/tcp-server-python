#!/usr/bin/env python

import imp

file = imp.load_source('file', '/lib/file.py')

class Sync(object):

	def init(self, server='127.0.0.1'):
		print ('starting the sync server to connect to %s', server)
