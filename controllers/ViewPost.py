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

class ViewPost(webapp2.RequestHandler):
	def get(self):
		trips = 0
		trip_posted = Trip.all()
		trip_posted.order("-time")
		
		for each in trip_posted:
			trips += 1

		params = {
			'trip_posted': trip_posted,
			'trips': trips
		}

		render_template(self, 'view.html', params)