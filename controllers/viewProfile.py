import webapp2
import os
import sys

from google.appengine.ext.webapp import template
from google.appengine.ext import ndb

def render_template(handler, templatename, templatevalues):
	path = os.path.join(os.path.dirname(__file__), "../templates/", templatename)
	html = template.render(path, templatevalues)
	handler.response.out.write(html)


class ViewProfile(webapp2.RequestHandler):
	def get(self):
		render_template(self, 'profile.html', {})