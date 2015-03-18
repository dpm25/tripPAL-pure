import webapp2
import os

from google.appengine.api import users

class LogoutHandler (webapp2.RequestHandler):
	def get(self):
		self.redirect(users.create_logout_url("/"))