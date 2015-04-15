
from google.appengine.ext import ndb

class Trip (ndb.Model):
	name = ndb.StringProperty()
	creator = ndb.StringProperty()
	
	origin_city = ndb.StringProperty()
	origin_state = ndb.StringProperty()
	origin_zip = ndb.StringProperty()
	
	dest_streetnum = ndb.IntegerProperty(indexed = True)
	dest_route = ndb.StringProperty(indexed = True)
	dest_city = ndb.StringProperty(indexed = True)
	dest_state = ndb.StringProperty()
	dest_zip = ndb.StringProperty()
	
	contact = ndb.StringProperty()
	description = ndb.StringProperty()
	time = ndb.IntegerProperty()