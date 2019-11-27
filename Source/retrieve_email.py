import easyimap
import imaplib

mail = imaplib.IMAP4_SSL('imap.gmail.com')

##
# @brief Gmail_imap class to create imap object and perform actions.
#
class Gmail_imap:

	##
	# @brief init()
	#
	# @details init() to stabilise connection with gmail imap server
	#
	# @param[in]    userid    user email id
	# @param[in]    password    password for login
	#
	def __init__(self, userid, password):

		self.userid=userid
		self.password=password
		self.imapper = easyimap.connect('imap.gmail.com', userid, password)

	##
	# @brief Retrieve mails
	#
	# @details Function to retrieve all mails in mailbox
	#
	def get_allmail(self):

		l = []
		for mail_id in self.imapper.listids(limit=100):
			mail = self.imapper.mail(mail_id)
			l.append(mail)
		return l

	##
	# @brief Fetch Mail Ids
	#
	# @details This function retrieve mails based on mail id(s)
	#
	# @param[in]    ids    user email id(s)
	#
	def fetch_mail_id(self, ids) :
		mail_list=[]
		for i in  ids:
			mail_list.append(self.imapper.mail(i))
		#print("mails=====\n",list)
		return  mail_list

	##
	# @brief Fetch Unseen mails
	#
	# @details Retrieve all the unseen mail from mailbox.
	#
	def get_unseenmail(self):
		mail.login(self.userid, self.password)
		mail.select("inbox")
		rv, msgset = mail.search(None, 'UNSEEN')
		id_list =msgset[0].split()
		print(rv, " -----------------------\n", msgset[0].split())
		mail.close()
		mail.logout()
		return id_list

	##
	# @brief Logout
	#
	# @details logout from current account
	#

	def account_logout(self,):
		self.imapper.quit()

	# def change_mailbox(self,mailbox):
	# 	self.imapper.change_mailbox(mailbox)

	##
	# @brief Delete Mail
	#
	# @details deletes a mail with given subject and sender mail address.
	#
	# @param[in]    fromID    sender mail address
	# @param[in]    subject    subject of mail to be deleted
	#
	def delete_mail(self,fromID, subject=None):
		mail.login(self.userid,self.password)
		mail.select("inbox")
		frm='FROM '+fromID

		#print(sub,"-============\n")
		if(subject == None):
			rv, msgset= mail.search(None, frm)
		else:
			sub = 'SUBJECT ' + subject
			rv, msgset = mail.search(None, frm, sub)
		print(rv," -----------------------\n", msgset)
		if(len(msgset) !=0):
			for i in msgset[0].split():
				print("deleting\t", i,"\n")
				mail.store(i, '+FLAGS', '\\Deleted')
		mail.close()
		mail.logout()

	
