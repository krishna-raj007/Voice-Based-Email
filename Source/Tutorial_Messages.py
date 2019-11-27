##
# @brief The text-to-speech
#



import text_to_speech as ts
##
# @brief Tutorial Messages
#
# @details class to access various tutorial sentences/speeches.This manages all sentences of the application to let user get commands
#
#

class Tutorial_Messages:


    ##
    # @details Commands available to user on dashboard i.e. compose, inbox, logout.
    #
    def dashboard_msg(self):
        ts.t2s("Welcome to your email account.   Please listen your choices.   Compose to  compose.  Inbox to access your  inbox. Logout to  logout form this account ")

    ##
    # @details Commands available to user to choose mailboxes i.e.inbox, sent box, important, drafts.
    #
    def mailboxes_msg(self,):
        ts.t2s("This is your mailbox.   Please listen your choices.   Inbox to choose inbox.  Sent to choose sent box. Important to choose important mailbox. Drafts to choose draftbox.")

    ##
    # @details Commands available to user on inbox i.e. read all, read unseen.
    #
    def inbox_msg(self,):
        ts.t2s("Welcome to your inbox. Please listen your choice.  Read all k to read all mails. Unseen to read unseen mails.")

    ##
    # @details Commands available to user while reading a mail i.e. read entire mail, reply, forward, delete, read next, stop reading.
    #
    def readAll_msg(self,):
        ts.t2s("reading all mails give command after each mail information after you listen speak now, read to read complete message next to read next mail forward to forward mail Delete to delete mail reply to reply mail stop to stop reading all mails.")

    ##
    # @details Commands available to user when on  mailbox i.e. sent box, important.
    #
    def box_msg(self,):

        ts.t2s("Please listen your choice.  Read all  to read all mails. Dashboard to go to your mail dashboard.")