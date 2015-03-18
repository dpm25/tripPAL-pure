import webapp2
import os
from google.appengine.api import mail
from google.appengine.ext.webapp import template
from google.appengine.api import users

def render_template(handler, templatename, templatevalues):
	path = os.path.join(os.path.dirname(__file__), "../templates/", templatename)
	html = template.render(path, templatevalues)
	handler.response.out.write(html)

class ContactUs(webapp2.RequestHandler):

	def get(self):
		render_template(self, 'contactUs.html', {})

	def post(self):
		
		from_email = self.request.get("from") 
		user = users.get_current_user()
		user_email = user.email()
		if from_email == user_email:
			to = "pitttrippal@gmail.com"
			subject = self.request.get("subject")
			body = self.request.get("message")

			#if not is_email_valid(from_email):
			#	from_email = "pitttrippal@gmail.com"


			mail.send_mail(from_email, to, subject, body)
			render_template(self, 'index.html', {})
		else:
			to = "pitttrippal@gmail.com"
			subject = self.request.get("subject")
			body = from_email + " --- " + self.request.get("message")
			mail.send_mail(to, to, subject, body)
			render_template(self, 'index.html', {})


