
from google.appengine.ext import ndb

class Trip (ndb.Model):
	name = db.StringProperty()
	
	origin_city = db.StringProperty()
	origin_state = db.StringProperty()
	origin_zip = db.IntegerProperty()
	
	dest_city = db.StringProperty(indexed = True)
	dest_state = db.StringProperty()
	dest_zip = db.StringProperty()
	
	description = db.StringProperty(multiline = True)
	time = db.IntegerProperty()