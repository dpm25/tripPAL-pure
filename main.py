import webapp2
import os
import sys

from google.appengine.ext.webapp import template
from google.appengine.ext import db

class Trip (db.Model):
	trip_owner = db.StringProperty()
	origin = db.StringProperty()
	destination = db.StringProperty()
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
		trip.trip_owner = self.request.get('name')
		trip.origin = self.request.get('origin')
		trip.destination = self.request.get('destinaton')
		trip.contact = self.request.get('contactInfo')
		trip.description = self.request.get('description')
		trip.time = int(time.time())
		trip.put()
		self.redirect('/')
		

app = webapp2.WSGIApplication([
    ('/', MainPage),
	('/makePost', MakePost),
	('/acceptPost', AcceptPost)
], debug=True)
