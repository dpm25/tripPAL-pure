import webapp2
import os
import sys
import time

from google.appengine.ext.webapp import template
from google.appengine.ext import ndb
from google.appengine.api import users

from model.Trip import *
from model.Commute import *

def render_template(handler, templatename, templatevalues):
	path = os.path.join(os.path.dirname(__file__), "../templates/", templatename)
	html = template.render(path, templatevalues)
	handler.response.out.write(html)

class AcceptPost(webapp2.RequestHandler):
	def post(self):
		choice = self.request.get('type')
		user = users.get_current_user()
		if choice == 't':
			trip = Trip()
			trip.name = self.request.get('name')
			trip.creator = user.nickname()
			trip.origin_city = self.request.get('origin_city')
			trip.origin_state = self.request.get('origin_state')
			trip.origin_zip = self.request.get('origin_zip')
			trip.dest_city = self.request.get('dest_city')
			trip.dest_state = self.request.get('dest_state')
			trip.dest_zip = self.request.get('dest_zip')
			trip.contact = self.request.get('contactInfo')
			trip.description = self.request.get('description')
			trip.time = int(time.time())
			trip.put()
		
		elif choice == 'c':
			commute = Commute()
			commute.name = self.request.get('name_commute')
			commute.creator = user.nickname()
			commute.origin_city = self.request.get('origin_city_commute')
			commute.origin_state = self.request.get('origin_state_commute')
			commute.origin_zip = self.request.get('origin_zip_commute')
			commute.dest_city = self.request.get('dest_city_commute')
			commute.dest_state = self.request.get('dest_state_commute')
			commute.dest_zip = self.request.get('dest_zip_commute')
			commute.description = self.request.get('description_commute')
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