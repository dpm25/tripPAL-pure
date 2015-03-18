import webapp2
import os
from google.appengine.api import mail
from google.appengine.ext.webapp import template

from google.appengine.api import users
from google.appengine.ext import ndb

from model.User import *

def render_template(handler, templatename, templatevalues):
	path = os.path.join(os.path.dirname(__file__), "../templates/", templatename)
	html = template.render(path, templatevalues)
	handler.response.out.write(html)

class WeeklyMail(webapp2.RequestHandler):

	def get(self):
		
		users = UserInfo.query()

		for user in users:
			sender = 'pitttrippal@gmail.com'
			to = user.nickname + '@gmail.com'
			subject = 'CS 1520 is at 6 pm on Wednesday nights'
			body = 'Make sure you take good notes. Just a friendly reminder from your good friends at tripPAL.'
			mail.send_mail(sender=sender, to=to, subject=subject, body=body)
		