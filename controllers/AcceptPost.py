import webapp2
import os
import sys
import time

from google.appengine.ext.webapp import template
from google.appengine.ext import ndb

from model.Trip import *
from model.Commute import *

def render_template(handler, templatename, templatevalues):
	path = os.path.join(os.path.dirname(__file__), "../templates/", templatename)
	html = template.render(path, templatevalues)
	handler.response.out.write(html)

class AcceptPost(webapp2.RequestHandler):
	def post(self):
		choice = self.request.get('type')
		if choice == 't':
			trip = Trip()
			trip.name = self.request.get('name')
			trip.origin_city = self.request.get('origin_city')
			trip.origin_state = self.request.get('origin_state')
			trip.origin_zip = int(self.request.get('origin_zip'))
			trip.dest_city = self.request.get('dest_city')
			trip.dest_state = self.request.get('dest_state')
			trip.dest_zip = int(self.request.get('dest_zip'))
			trip.contact = self.request.get('contactInfo')
			trip.description = self.request.get('description')
			trip.time = int(time.time())
			trip.put()
		
		elif choice == 'c':
			commute = Commute()
			commute.name = self.request.get('name')
			commute.origin_city = self.request.get('origin_city')
			commute.origin_state = self.request.get('origin_state')
			commute.origin_zip = int(self.request.get('origin_zip'))
			commute.dest_city = self.request.get('dest_city')
			commute.dest_state = self.request.get('dest_state')
			commute.dest_zip = int(self.request.get('dest_zip'))
			commute.description = self.request.get('description')
			monday = self.request.get('monday')
			if monday:
				commute.monday = True
			else:
				commute.monday = False
			tuesday = self.request.get('tuesday')
			if tuesday:
				commute.tuesday = True
			else:
				commute.tuesday = False
			wednesday = self.request.get('wednesday')
			if wednesday:
				commute.wednesday = True
			else:
				commute.wednesday = False
			thursday = self.request.get('thursday')
			if thursday:
				commute.thursday = True
			else:
				commute.thursday = False
			friday = self.request.get('friday')
			if friday:
				commute.friday = True
			else:
				commute.friday = False
			saturday = self.request.get('saturday')
			if saturday:
				commute.saturday = True
			else:
				commute.saturday = False
			sunday = self.request.get('sunday')
			if sunday:
				commute.sunday = True
			else:
				commute.sunday = False
			commute.put()
			
		self.redirect('/')