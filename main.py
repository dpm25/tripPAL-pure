import webapp2
import os
import sys
import time

from google.appengine.ext.webapp import template
from google.appengine.ext import db

class Trip (db.Model):
	name = db.StringProperty()
	origin_city = db.StringProperty()
	origin_state = db.StringProperty()
	origin_zip = db.StringProperty()
	dest_city = db.StringProperty()
	dest_state = db.StringProperty()
	dest_zip = db.StringProperty()
	contact = db.StringProperty()
	description = db.StringProperty(multiline = True)
	time = db.IntegerProperty()
	
def render_template(handler, templatename, templatevalues):
	path = os.path.join(os.path.dirname(__file__), "templates/", templatename)
	html = template.render(path, templatevalues)
	handler.response.out.write(html)

class MainPage(webapp2.RequestHandler):
    def get(self):
        render_template(self, 'index.html', {})
		
class MakePost(webapp2.RequestHandler):
	def get(self):
		render_template(self, 'post.html', {})

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

class viewPost(webapp2.RequestHandler):
	def get(self):

		trip_posted = Trip.all()
		trip_posted.order("-time")

		params = {
			'trip_posted': trip_posted
		}

		render_template(self, 'view.html', params)

app = webapp2.WSGIApplication([
    ('/', MainPage),
	('/makePost', MakePost),
	('/acceptPost', AcceptPost),
	('/viewPost', viewPost),
], debug=True)
