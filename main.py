import webapp2

from google.appengine.ext.webapp import template
from google.appengine.ext import db

from controllers.SearchPost import *
from controllers.AcceptPost import *
from controllers.ViewPost import *
from controllers.MakePost import *

def render_template(handler, templatename, templatevalues):
	path = os.path.join(os.path.dirname(__file__), "templates/", templatename)
	html = template.render(path, templatevalues)
	handler.response.out.write(html)

class MainPage(webapp2.RequestHandler):
    def get(self):
        render_template(self, 'index.html', {})
        
app = webapp2.WSGIApplication([
    ('/', MainPage),
	('/makePost', MakePost),
	('/acceptPost', AcceptPost),
	('/viewPost', ViewPost),
	('/searchPost', SearchPost)
], debug=True)
