from google.appenginge.ext import ndb

class Commute (ndb.Model):
	name = ndb.StringProperty()
	
	origin_address = ndb.StringProperty()
	origin_city = ndb.StringProperty()
	origin_state = ndb.StringProperty()
	origin_zip = ndb.IntegerProperty()
	
	dest_address = ndb.StringProperty(indexed = True)
	dest_city = ndb.StringProperty(indexed = True)
	dest_state = ndb.StringProperty()
	dest_zip = ndb.IntegerProperty(indexed = True)
	
	description = ndb.StringProperty(multiline = True)
	date = ndb.DateTimeProperty (auto_now = True)
	
	monday = ndb.BooleanProperty()
	tuesday = ndb.BooleanProperty()
	wednesday = ndb.BooleanProperty()
	thursday = ndb.BooleanProperty()
	friday = ndb.BooleanProperty()
	saturday = ndb.BooleanProperty()
	sunday = ndb.BooleanProperty()