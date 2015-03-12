
from google.appengine.ext import ndb

class Trip (ndb.Model):
	name = ndb.StringProperty()
	
	origin_city = ndb.StringProperty()
	origin_state = ndb.StringProperty()
	origin_zip = ndb.IntegerProperty()
	
	dest_city = ndb.StringProperty(indexed = True)
	dest_state = ndb.StringProperty()
	dest_zip = ndb.IntegerProperty()
	
	description = ndb.StringProperty()
	time = ndb.IntegerProperty()