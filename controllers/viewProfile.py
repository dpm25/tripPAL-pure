import webapp2
import os
import sys

from google.appengine.ext.webapp import template
from google.appengine.ext import ndb
from google.appengine.api import users

from model.User import *


def render_template(handler, templatename, templatevalues):
	path = os.path.join(os.path.dirname(__file__), "../templates/", templatename)
	html = template.render(path, templatevalues)
	handler.response.out.write(html)


class ViewProfile(webapp2.RequestHandler):
	def get(self):
		user = users.get_current_user()
		nName = user.nickname()

		q = UserInfo.query(UserInfo.nickname == nName).fetch()
		if not q:
			self.redirect('/')
		else:
			firstName = q[0].firstName
			lastName = q[0].lastName
			phone = q[0].phone
			address = q[0].address
			city = q[0].city
			state = q[0].state
			zip = q[0].zip

			params = {
				'tab':		2,
				'user': 	user,
				'firstname': firstName,
				'lastname': lastName,
				'phone': phone,
				'address': address,
				'city': city,
				'state': state,
				'zip': zip	
			}
			render_template(self, 'profile.html', params)