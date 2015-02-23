import webapp2
import os
import sys
import time

from google.appengine.ext.webapp import template
from google.appengine.ext import db

from model.Trip import *

def render_template(handler, templatename, templatevalues):
	path = os.path.join(os.path.dirname(__file__), "../templates/", templatename)
	html = template.render(path, templatevalues)
	handler.response.out.write(html)

class MakePost(webapp2.RequestHandler):
	def get(self):
		render_template(self, 'post.html', {})