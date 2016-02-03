from django.db import models

class MandrillParam(object):


        """
             'from_email': 'it@mofilm.com',
             'from_name': 'MOFILM',
             'html': '<p>Example HTML content</p>',
             'subject': 'example subject',
             'text': 'Example text content',
             'to': [{'email': 'm.mithun@gmail.com',
                     'name': 'Recipient Name',
                     'type': 'to'}],

        """
        def __init__(self, fromEmail, fromName, html, subject, textData, toEmail, toName):
                self.fromEmail = fromEmail
                self.fromName = fromName
                self.html = html
                self.subject = subject
                self.textData = textData
                self.toEmail = toEmail
                self.toName = toName

        def getMandrillMessage(self):
                message = {}
                message["from_name"] = self.fromName
                message["from_email"] = self.fromEmail
                message["html"] = self.html
                message["subject"] = self.subject
                message["text"] = self.textData
                sendData = []
                toData = {}
                toData["email"] = self.toEmail
                toData["name"] = self.toName
                toData["type"] = "to"
                sendData.append(toData)
                print sendData
                message["to"] = sendData
                return message



