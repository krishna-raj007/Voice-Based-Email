import easyimap
imapper=''
def connection(userid,password):
	imapper = easyimap.connect('imap.gmail.com', login, password)

def compose_mail():
	#imp
	pass
def send_mail(targets,msg):
    #the function should take take user name and password and return the contents of inbox
    #in a format that we can extract mails from it
    raise NotImplemented

def get_inbox():
	
	for mail_id in imapper.listids(limit=100):
	    mail = imapper.mail(mail_id)
	    print(mail.from_addr)
	    print(mail.to)
	    print(mail.cc)
	    print(mail.title)
	    print(mail.body)
	    print(mail.attachments)
def logout():
	imapper.quit()
	
