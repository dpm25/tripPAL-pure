import webapp2
import os
import sys
import time
import logging

from google.appengine.ext.webapp import template
from google.appengine.ext import ndb

from model.Trip import *
from model.Commute import *

def render_template(handler, templatename, templatevalues):
	path = os.path.join(os.path.dirname(__file__), "../templates/", templatename)
	html = template.render(path, templatevalues)
	handler.response.out.write(html)

class SearchPost (webapp2.RequestHandler):
	def post (self):
		street_number = self.request.get('street_number')
		route = self.request.get('route')
		logging.info("hello route" + route)
		locality = self.request.get('locality')
		logging.info("hello locality" + locality)
		kind = self.request.get('type')

		user_input = self.request.get('searchBar')

		if (route is None or route == ""):
			if kind == "Trip":
				q = Trip.query().filter(Trip.dest_city == user_input).order(-Trip.time).fetch()
		
			elif kind == "Commute":
				q = Commute.query().filter(Commute.dest_city == user_input).order(-Commute.date).fetch()
		else:
			logging.info("do we get here")
			if kind == "Trip":
				q = Trip.query().filter(Trip.dest_route == route).order(-Trip.time).fetch()
		
			elif kind == "Commute":
				q = Commute.query().filter(Commute.dest_address == route).order(-Commute.date).fetch()

			if (not q):
				if kind == "Trip":
					q = Trip.query().filter(Trip.dest_city == locality).order(-Trip.time).fetch()
		
				elif kind == "Commute":
					q = Commute.query().filter(Commute.dest_address == locality).order(-Commute.date).fetch()

		
		trips = 0
	
		for each in q:
			trips +=1
			
		params = {
			'trip_posted': q,
			'trips': trips,
			'type': kind
		}
		render_template(self, 'search.html', params)