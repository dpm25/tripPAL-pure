from google.appengine.ext import ndb

class Comment (ndb.Model):
	date = ndb.DateTimeProperty (auto_now = True)
	poster = ndb.StringProperty()
	parent_id = ndb.StringProperty()
	message = ndb.StringProperty()
	
	