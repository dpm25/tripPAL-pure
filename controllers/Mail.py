import webapp2
import os
from google.appengine.api import mail
from google.appengine.ext.webapp import template

def render_template(handler, templatename, templatevalues):
	path = os.path.join(os.path.dirname(__file__), "../templates/", templatename)
	html = template.render(path, templatevalues)
	handler.response.out.write(html)

class ContactUs(webapp2.RequestHandler):

	def get(self):
		render_template(self, 'contactUs.html', {})

	def post(self):
		
		from_email = self.request.get("from") 
		to = "pitttrippal@gmail.com"
		subject = self.request.get("subject")
		body = self.request.get("message")

		#if not is_email_valid(from_email):
		#	from_email = "pitttrippal@gmail.com"


		mail.send_mail(from_email, to, subject, body)
		render_template(self, 'index.html', {})


