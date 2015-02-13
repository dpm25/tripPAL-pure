import webapp2
import os
import sys

from google.appengine.ext.webapp import template

def render_template(handler, templatename, templatevalues):
	path = os.path.join(os.path.dirname(__file__), "templates/", templatename)
	html = template.render(path, templatevalues)
	handler.response.out.write(html)

class MainPage(webapp2.RequestHandler):
    def get(self):
        render_template(self, 'index.html', {})
		
class MakePost(webapp2.RequestHandler):
	def get(self):
		render_template(self, 'post.html', {})

app = webapp2.WSGIApplication([
    ('/', MainPage),
	('/makepost', MakePost),
	
], debug=True)
