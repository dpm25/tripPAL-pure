import webapp2
import os
import sys
import time

from google.appengine.ext.webapp import template
from google.appengine.ext import db

from model.Trip import *

def render_template(handler, templatename, templatevalues):
	path = os.path.join(os.path.dirname(__file__), "../templates/", templatename)
	html = template.render(path, templatevalues)
	handler.response.out.write(html)

class SearchPost (webapp2.RequestHandler):
	def post (self):
		trips = 0
		search = self.request.get('searchBar')
		q = Trip.all()
		q.filter('dest_city =', search)
		q.order('-time')
		
		for each in q:
			trips +=1
			
		params = {
			'trip_posted': q,
			'trips': trips
		}
		render_template(self, 'search.html', params)