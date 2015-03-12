from google.appengine.ext import ndb

# class for UserInfo data model
class UserInfo(ndb.Model):
	userName = ndb.StringProperty()
	nickname = ndb.StringProperty()
	firstName = ndb.StringProperty()
	lastName = ndb.StringProperty()
	phone = ndb.StringProperty()
	address = ndb.StringProperty()
	city = ndb.StringProperty()
	state = ndb.StringProperty()
	zip = ndb.StringProperty()
	time = ndb.IntegerProperty()