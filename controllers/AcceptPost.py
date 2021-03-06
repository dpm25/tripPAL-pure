import webapp2
import os
import sys
import time

from google.appengine.ext.webapp import template
from google.appengine.ext import ndb
from google.appengine.api import users

from model.Trip import *
from model.Commute import *

def render_template(handler, templatename, templatevalues):
	path = os.path.join(os.path.dirname(__file__), "../templates/", templatename)
	html = template.render(path, templatevalues)
	handler.response.out.write(html)

class AcceptPost(webapp2.RequestHandler):
	def post(self):
		#errors is going to contain list of errors from the form
		errors=[]
		# get form vars for validation checking in trip form
		name = self.request.get('name')
		city = self.request.get('origin_city')
		streetNum = self.request.get('streetNum')
		route = self.request.get('route')
		dest_city = self.request.get('dest_city')
		dest_state = self.request.get('dest_state')
		description = self.request.get('description')

		# get form vars for validation checking in commute form
		name_commute = self.request.get('name_commute')
		origin_city_commute = self.request.get('origin_city_commute')
		streetNum_commute = self.request.get('streetNum_commute')
		route_commute = self.request.get('route_commute')
		dest_city_commute = self.request.get('dest_city_commute')
		dest_state_commute = self.request.get('dest_state_commute')
		description_commute = self.request.get('description_commute')

		if 'javascript' in name or '<' in name or '<script>' in name:
			errors+=["invalid"]
		if 'javascript' in city or '<' in city or '<script>' in city:
			errors+=["invalid"]
		if 'javascript' in streetNum or '<' in streetNum or '<script>' in streetNum:
			errors+=["invalid"]
		if 'javascript' in route or '<' in route or '<script>' in route:
			errors+=["invalid"]
		if 'javascript' in dest_city or '<' in dest_city or '<script>' in dest_city:
			errors+=["invalid"]
		if 'javascript' in dest_state or '<' in dest_state or '<script>' in dest_state:
			errors+=["invalid"]
		if 'javascript' in description or '<' in description or 'update' in description or 'delete' in description or '<script>' in description:
			errors+=["invalid"]
		if 'javascript' in name_commute or '<' in name_commute or '<script>' in name_commute:
			errors+=["invalid"]
		if 'javascript' in origin_city_commute or '<' in origin_city_commute or '<script>' in origin_city_commute:
			errors+=["Name is invalid"]
		if 'javascript' in streetNum_commute or '<' in streetNum_commute or '<script>' in streetNum_commute:
			errors+=["invalid"]
		if 'javascript' in route_commute or '<' in route_commute or '<script>' in route_commute:
			errors+=["invalid"]
		if 'javascript' in dest_city_commute or '<' in dest_city_commute or '<script>' in dest_city_commute:
			errors+=["invalid"]
		if 'javascript' in dest_state_commute or '<' in dest_state_commute or '<script>' in dest_state_commute:
			errors+=["invalid"]
		if 'javascript' in description_commute or '<' in description_commute or 'update' in description_commute or 'delete' in description_commute or '<script>' in description_commute:
			errors+=["invalid"]

		# if errors in the form
		if len(errors)>0:
			for error in errors:
				render_template(self, 'error.html', {})

		else:		
			choice = self.request.get('type')
			user = users.get_current_user()
			if choice == 't':
				trip = Trip()
				trip.name = self.request.get('name')
				trip.creator = user.nickname()
				trip.origin_city = self.request.get('origin_city')
				trip.origin_state = self.request.get('origin_state')
				trip.origin_zip = self.request.get('origin_zip')
				trip.dest_city = self.request.get('dest_city')
				trip.dest_state = self.request.get('dest_state')
				trip.dest_zip = self.request.get('dest_zip')
				trip.contact = self.request.get('contactInfo')
				trip.description = self.request.get('description')
				trip.dest_streetnum = int(self.request.get('streetNum'))
				trip.dest_route = self.request.get('route')
				trip.time = int(time.time())
				trip.put()
			
			elif choice == 'c':
				commute = Commute()
				commute.name = self.request.get('name_commute')
				commute.creator = user.nickname()
				commute.origin_city = self.request.get('origin_city_commute')
				commute.origin_state = self.request.get('origin_state_commute')
				commute.origin_zip = self.request.get('origin_zip_commute')
				commute.dest_city = self.request.get('dest_city_commute')
				commute.dest_state = self.request.get('dest_state_commute')
				commute.dest_zip = self.request.get('dest_zip_commute')
				commute.description = self.request.get('description_commute')
				commute.dest_streetnum = int(self.request.get('streetNum_commute'))
				commute.dest_address = self.request.get('route_commute')
				monday = self.request.get('monday')
				if monday:
					commute.monday = True
				else:
					commute.monday = False
				tuesday = self.request.get('tuesday')
				if tuesday:
					commute.tuesday = True
				else:
					commute.tuesday = False
				wednesday = self.request.get('wednesday')
				if wednesday:
					commute.wednesday = True
				else:
					commute.wednesday = False
				thursday = self.request.get('thursday')
				if thursday:
					commute.thursday = True
				else:
					commute.thursday = False
				friday = self.request.get('friday')
				if friday:
					commute.friday = True
				else:
					commute.friday = False
				saturday = self.request.get('saturday')
				if saturday:
					commute.saturday = True
				else:
					commute.saturday = False
				sunday = self.request.get('sunday')
				if sunday:
					commute.sunday = True
				else:
					commute.sunday = False
				commute.put()
				
			self.redirect('/')