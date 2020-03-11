import requests
import json
import smtplib
from smtplib import SMTPException

class WebSiteRunning:
	
	website = ""
	reportingPerson = ""
	filename = ""
	
	def __init__(self, website, reportingPerson, filename):
		self.website = website
		self.reportingPerson = reportingPerson
		self.filename = filename

	def websiteResponse(self):
		response = requests.get(self.website)
		if response.ok == True:
			print(self.website, " is Running")
			self.writeWebSiteResponse(response.text)
		else:
			self.sendWaringEmail()		

	def writeWebSiteResponse(self, data):
		newfilename = f"dummyFiles/{self.filename}"
		newFile = open(newfilename, "a+")
		newFile.write(data)

	def sendWaringEmail(self):
		sender = 'no-reply@3pillarglobal.com'
		receivers = ['imran.gnit@gmail.com']

		message = """From: From Person <cronjob@3pillarglobal.com>
		To: To Person <to@todomain.com>
		Subject: SMTP e-mail test

		This is a test e-mail message.
		"""

		try:
			smtpObj = smtplib.SMTP('localhost')
			smtpObj.sendmail(sender, receivers, message)         
			print ("Successfully sent email")
		except SMTPException:
			print ("Error: unable to send email")
		except ConnectionRefusedError:
			print("SMTP server is not running. Contact to administrator")	

		

objWS1 = WebSiteRunning("http://dummy.restapiexample.com/api/v1/employees", "mohammad.imran@3pillarglobal.com", "first_website.json")
objWS1.websiteResponse()

objWS2 = WebSiteRunning("https://in.yahoo.com/?p=us", "imran.gnit@gmail.com", "second_website.txt")
objWS2.websiteResponse()

objWS3 = WebSiteRunning("https://www.flipkart.com/", "ikram.bahraich@gmail.com", "third_website.txt")
objWS3.websiteResponse()