import webapp2
import os
import sys
import time

from google.appengine.ext.webapp import template
from google.appengine.ext import ndb
from google.appengine.api import users

from model.User import *
from model.Trip import *
from model.Commute import *

class ToggleHandler (webapp2.RequestHandler):
	def post(self):
		id = self.request.get('key')
		kind = self.request.get('type')

		if kind == "Trip":
			temp = ndb.Key("Trip", int(id)).get()

		if kind == "Commute":
			temp = ndb.Key("Commute", int(id)).get()

		if (temp.opened):
			temp.opened = false
			opened = 0
		else:
			temp.opened = true
			opened = 1

		temp.put()

		result = []
		tmp = {}
		tmp['status'] = opened
		result += [tmp]

		self.response.write(json.dumps(result))