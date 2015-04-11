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

		# getting all the form values
		fname = self.request.get('fname')
		lname = self.request.get('lname')
		phone = self.request.get('phone')
		address = self.request.get('address')
		city = self.request.get('city')
		state = self.request.get('state')
		zip = self.request.get('zip')

		# errors is going to contain list of errors from the form
		errors=[]

		# checking if the first and last name exist
		if fname is None or fname=="":
			errors+=["First Name is missing"]
		if lname is None or fname=="":
			errors+=['last name is missing']
		# checking the length of the phone number
		if len(phone)<10 or len(phone)>11:
			errors+=["invalid phone number"]
		# checking is the address, city, state, and zip exists
		if address is None or address=="":
			errors+=["address is missing"]
		if city is None or city=="":
			errors+=["city is missing"]
		if state is None or state=="":
			errors+=["invalid or missing state"]
		if len(zip)!=5:
			errors+=["invalid or missing zip"]

		if len(errors)>0:
			for error in errors:
				render_template(self, 'contactUs.html', {})
		# if no errors in form
		else:
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
		