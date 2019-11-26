
# import imaplib
# import ssl
# import email.message
# import email.charset
# import time
# tls_context = ssl.create_default_context()
# server = imaplib.IMAP4('imap.gmail.com')
# server.starttls(ssl_context=tls_context)
# server.login('vinodassignmentiitb@gmail.com', 'assignments@vinod')
# # Select mailbox
# server.select("INBOX.Drafts")
# # Create message
# new_message = email.message.Message()
# new_message["From"] = "Your name <vinodassignmentiitb@gmail.com>"
# new_message["To"] = "Name of Recipient <gaurav.singh.atoria@gmail.com>"
# new_message["Subject"] = "Your subject"
# new_message.set_payload("""
# This is your message.
# It can have multiple lines and
# contain special characters: äöü.
# """)
# # Fix special characters by setting the same encoding we'll use later to encode the message
# new_message.set_charset(email.charset.Charset("utf-8"))
# encoded_message = str(new_message).encode("utf-8")
# server.append('INBOX.Drafts', '', imaplib.Time2Internaldate(time.time()), encoded_message)
# # Cleanup
# server.close()



import time
import random
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import imaplib
msg = MIMEMultipart("alternative")
msg.set_charset("utf-8")
body="Hello"
msg.attach(MIMEText(body, "plain", "utf-8"))
msg['Subject'] = "SUBJECT"
msg['From'] = "vinodassignmentiitb@gmail.com"
msg['To'] = "rajsrivastava871@gmail.com"

conn = imaplib.IMAP4_SSL('imap.gmail.com', port = 993)
conn.login('vinodassignmentiitb@gmail.com', 'assignments@vinod')
conn.select('[Gmail]/Drafts')
conn.append("[Gmail]/Drafts",'',imaplib.Time2Internaldate(time.time()),msg.as_bytes())