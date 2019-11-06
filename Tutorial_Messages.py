import text_to_speech as ts
# class Tutorial_Messages:
def dashboard_msg():
    ts.t2s("Welcome to your email account. Please listen your choices Single left click to compose Single right to inbox Double right click to logout")


def inbox_msg():
    ts.t2s("Welcome to your inbox. Please listen your choice Single left click to read all mails right click to go to dashboard")

def readAll_msg():
	ts.t2s("reading all mails please give command after each mail information and your commands are ")
def readAll_cmds():
    ts.t2s("read to read complete message next to read next mail forward to forward mail Delete to delete mail reply to reply mail stop to stop reading all mails and go to inbox and help to listen commands")
