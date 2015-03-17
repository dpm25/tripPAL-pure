import webapp2
import os

from google.appengine.ext.webapp import template
from google.appengine.ext import db
from google.appengine.api import users

from controllers.SearchPost import *
from controllers.AcceptPost import *
from controllers.ViewPost import *
from controllers.MakePost import *
from controllers.Profile import *
from controllers.viewProfile import *
from controllers.Mail import *
from controllers.saveComment import *
from controllers.fetchHandler import *
from controllers.ViewEntityHandler import *

def render_template(handler, templatename, templatevalues):
	path = os.path.join(os.path.dirname(__file__), "templates/", templatename)
	html = template.render(path, templatevalues)
	handler.response.out.write(html)

class HomePageHandler(webapp2.RequestHandler):

	def get(self):
		# get current user of logged in to google
		user = users.get_current_user()
		email = 'unregister user'

		# check if exists
		if not user:
			# otherwise redirect to login page
			self.redirect(users.create_login_url("/"))
		else:
			# checking if we have a UserInfo instance in database
			if self.is_registered(user):

				email = user.email()
				params = {
					'tab':			 1,
					'user':          user,
             		'email':         email
				}
				# yes -> getting the path for index.html
				render_template(self, 'index.html', params)

			else:
				params = {
					'tab':			 2,
					'user':          user,
             		'email':         email
				}
				render_template(self, 'profile.html', params)

	def is_registered(self,user):		
		# getting the userinfo object
		userinfo = UserInfo.query(UserInfo.userName == user.user_id()).fetch()		
		# checking if anything is returned from database -> if not it means is the first visit of user
		return len(userinfo)>0

app = webapp2.WSGIApplication([
    ('/', HomePageHandler),
	('/makePost', MakePost),
	('/acceptPost', AcceptPost),
	('/viewPost', ViewPost),
	('/searchPost', SearchPost),
	('/submitProfile', Profile),
	('/viewProfile', ViewProfile),
	('/contactUs', ContactUs),
	('/saveComment', saveComment),
	('/fetch', fetchHandler),
	('/view', ViewEntityHandler)
], debug=True)
