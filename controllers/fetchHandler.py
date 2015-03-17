import json
import webapp2
import logging

from google.appengine.ext import ndb
from google.appengine.api import users

from model.Comment import *
from model.Trip import *
from model.Commute import *

class fetchHandler (webapp2.RequestHandler):
	def get(self):
		id = self.request.get("id")
		type = self.request.get("type")
		logging.info("This should print out type: " + str(type))
		if type == "0":
			comments = Comment.query(ancestor=ndb.Key("Trip", int(id))).order(-Comment.date).fetch()
			#comments = Comment.query().filter(Comment.parent_id == id).order(-Comment.date).fetch()
		elif type == "1":
			comments = Comment.query(ancestor=ndb.Key("Commute", int(id))).order(-Comment.date).fetch()
			#comments = Comment.query().filter(Comment.parent_id == id).order(-Comment.date).fetch()
		result = []
		for comment in comments:
			tmp = {}
			tmp['message'] = comment.message
			tmp['poster'] = comment.poster
			result += [tmp]
		
		self.response.write(json.dumps(result))