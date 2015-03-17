import webapp2
import os
import sys
import time

from google.appengine.ext.webapp import template
from google.appengine.ext import ndb
from google.appengine.api import users

from model.User import *

def render_template(handler, templatename, templatevalues):
	path = os.path.join(os.path.dirname(__file__), "../templates/", templatename)
	html = template.render(path, templatevalues)
	handler.response.out.write(html)

class Profile(webapp2.RequestHandler):

	def post(self):
		# get current user
		user = users.get_current_user()
		nName = user.nickname()
		
		q = UserInfo.query(UserInfo.nickname == nName).fetch()

		if q:
			# populate existing Profile stored object
			profile = q[0]
			profile.userName = user.user_id()
			profile.nickname = user.nickname()
			profile.firstName = self.request.get('fname')
			profile.lastName = self.request.get('lname')
			profile.phone = self.request.get('phone')
			profile.address = self.request.get('address')
			profile.city = self.request.get('city')
			profile.state = self.request.get('state')
			profile.zip = self.request.get('zip')
			profile.time = int(time.time())
			profile.put()
		else:
			profile = UserInfo()
			profile.userName = user.user_id()
			profile.nickname = user.nickname()
			profile.firstName = self.request.get('fname')
			profile.lastName = self.request.get('lname')
			profile.phone = self.request.get('phone')
			profile.address = self.request.get('address')
			profile.city = self.request.get('city')
			profile.state = self.request.get('state')
			profile.zip = self.request.get('zip')
			profile.time = int(time.time())
			profile.put()
		
		render_template(self, 'index.html', {})