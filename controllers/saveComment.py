import webapp2
import json
import logging

from google.appengine.ext import ndb
from google.appengine.api import users

from model.Comment import *
from model.Trip import *
from model.Commute import *

class saveComment (webapp2.RequestHandler):
	def post(self):
	 id = self.request.get("id")
	 comment = self.request.get("comment")
	 user = users.get_current_user()
	 type = self.request.get("type")
	 parent = None
	 logging.info("print this type" + type)
	 
	 if type == "0":
		logging.info ("do we get in here")
		parent = ndb.Key("Trip", int(id))
	 elif type == "1":
		parent = ndb.Key("Commute", int(id))
		logging.info ("or in here?")
	
	 com = Comment(poster = user.nickname(), message = comment, parent = parent, parent_id = id) 
	 com.put()

