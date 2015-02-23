
from google.appengine.ext import db

class Trip (db.Model):
	name = db.StringProperty()
	origin_city = db.StringProperty()
	origin_state = db.StringProperty()
	origin_zip = db.StringProperty()
	dest_city = db.StringProperty()
	dest_state = db.StringProperty()
	dest_zip = db.StringProperty()
	contact = db.StringProperty()
	description = db.StringProperty(multiline = True)
	time = db.IntegerProperty()