import easyimap

class Gmail_imap:

	def __init__(self,userid,password):
		self.imapper = easyimap.connect('imap.gmail.com', userid, password)

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

	
