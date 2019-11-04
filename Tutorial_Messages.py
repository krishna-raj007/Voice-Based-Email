import text_to_speech as ts
class Tutorial_Messages:
	def dashboard_msg(self):
	    ts.t2s("Welcome to your email account. Please listen your choices Single left click to compose Single right click to send Double left click to inbox Double right click to logout")


	def inbox_msg(self):
	    ts.t2s("Welcome to your inbox. Please listen your choice Single left click to read unseen mails Single right click to search mail Double left click to read all mails Double right click to go to dashboard")

	def readAll_msg(self):
	    ts.t2s("reading all mails give command after each mail information read to read complete message next to read next mail forward to forward mail Delete to delete mail stop to stop reading all mails and go to inbox")
