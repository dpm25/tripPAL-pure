import webapp2
import os

from google.appengine.ext.webapp import template
from google.appengine.ext import ndb
from google.appengine.api import users

def render_template(handler, templatename, templatevalues):
	path = os.path.join(os.path.dirname(__file__), "../templates/", templatename)
	html = template.render(path, templatevalues)
	handler.response.out.write(html)
	
class ViewEntityHandler (webapp2.RequestHandler):
	def get(self):
		id = self.request.get('id')
		kind = self.request.get('type')
		user = users.get_current_user()
		
		if not user:
			logged_in = 0
		else:
			logged_in = 1
		
		if kind == "Trip":
			entity = ndb.Key("Trip", int(id)).get()
			type = 0
		
		elif kind == "Commute":
			entity = ndb.Key("Commute", int(id)).get()
			type = 1
		
		params = {
			'entity': entity,
			'type': type,
			'logged_in': logged_in,
			'parent_id': id
		}
		render_template(self, 'entity.html', params)