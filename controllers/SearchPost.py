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
		type = self.request.get('type')
		search = self.request.get('searchBar')
		if type == "Trip":
			q = Trip.query().filter(Trip.dest_city == search).order(-Trip.time).fetch()
		
		elif type == "Commute":
			q = Commute.query().filter(Commute.dest_city == search).order(-Commute.date).fetch()
		
		trips = 0
	
		for each in q:
			trips +=1
			
		params = {
			'trip_posted': q,
			'trips': trips,
			'type': type
		}
		render_template(self, 'search.html', params)