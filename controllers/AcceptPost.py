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

class AcceptPost(webapp2.RequestHandler):
	def post(self):
		trip = Trip()
		trip.name = self.request.get('name')
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
		self.redirect('/')