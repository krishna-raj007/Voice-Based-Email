import easyimap
import imaplib
mail = imaplib.IMAP4_SSL('imap.gmail.com')

class Gmail_imap:

	def __init__(self,userid,password):
		"""init() to stabilise connection with gmail imap server .
		:param userid: gmail user id of user
		:type userid: string
		:param password: user account password
		:type password: string"""
		self.userid=userid
		self.password=password
		self.imapper = easyimap.connect('imap.gmail.com', userid, password)

	def get_allmail(self):
		"""Function to retrieve all mails in mailbox.
		:return l: list of mails
		:rtype l: mail object list"""
		l = []
		for mail_id in self.imapper.listids(limit=100):
			mail = self.imapper.mail(mail_id)
			l.append(mail)
		return l

	def fetch_mail_id(self, ids) :
		"""This function retrieve mails based on mail id(s)
		:param ids: list of mail id
		:type ids: binary
		:param mail_list: list mail objects
		:rtype mail_list: list"""
		mail_list=[]
		for i in  ids:
			mail_list.append(self.imapper.mail(i))
		#print("mails=====\n",list)
		return  mail_list

	def get_unseenmail(self):
		"""Retrieve all the unseen mail from mailbox.
		:return id_list: list of mail ids
		:rtype: id_list: list of binary"""
		mail.login(self.userid, self.password)
		mail.select("inbox")
		rv, msgset = mail.search(None, 'UNSEEN')
		id_list =msgset[0].split()
		print(rv, " -----------------------\n", msgset[0].split())
		mail.close()
		mail.logout()
		return id_list

	def account_logout(self,):
		"""logout from current account."""
		self.imapper.quit()

	def change_mailbox(self,mailbox):
		self.imapper.change_mailbox(mailbox)

	def delete_mail(self,fromID, subject):
		"""deletes a mail with given subject and sender mail address.
		:param fromID: sender mail address.
		:param subject: subject of mail to be deleted."""
		mail.login(self.userid,self.password)
		mail.select("inbox")
		frm="FROM "+fromID
		sub="SUBJECT "+subject
		print(frm,"-============\n")
		rv, msgset= mail.search(None,frm,sub)
		print(rv," -----------------------\n", msgset[0].split())
		l=msgset[0].split()
		mail.store(l[0], '+FLAGS', '\\Deleted')
		mail.close()
		mail.logout()

	
