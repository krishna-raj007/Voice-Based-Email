import easyimap

class Gmail:

	def __init__(self,userid,password):
		self.imapper = easyimap.connect('imap.gmail.com', userid, password)

	def compose_mail(self):
		print("in compose");
		#imp
		return
	def send_mail(self,targets,msg):
		print("iin send_mail")
	    #the function should take take user name and password and return the contents of inbox
	    #in a format that we can extract mails from it
	    #raise NotImplemented
		return
	def get_allmail(self):
		l=[]
		for mail_id in self.imapper.listids(limit=100):
		    mail = self.imapper.mail(mail_id)
		    l.append(mail)

		    # print(mail.from_addr)
		    # print(mail.to)
		    # print(mail.cc)
		    # print(mail.title)
		    # print(mail.body)
		    # print(mail.attachments)
		return l

	def get_unseenmail(self):
		l=[]
		for mail_id in self.imapper.unseen(limit=10):
			print("unseen")
			mail=self.imapper.mail(mail_id)
			l.append(mail)
		return l

	def logout(self):
		self.imapper.quit()
		return

	
