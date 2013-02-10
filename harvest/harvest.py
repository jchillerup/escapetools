#!/usr/bin/python2

import sys
import imaplib as imap
import pprint
import getpass
from mail_class import Mail

pp = pprint.PrettyPrinter(indent=4)
connection = imap.IMAP4_SSL("imap.gmail.com", 993)

print ":: Logging into GMail"

connection.login(raw_input("Username: "), getpass.getpass())

print ":: Logged in, enumerating mailboxes"

response, mailboxes = connection.list()

if response == "OK":
    for mailbox in mailboxes:
        print " - %s" % mailbox
else:
    print "Failed to enumerate mailboxes, exiting."
    sys.exit(1);


response, num_mails = connection.select("[Gmail]/All Mail", True)

if response == "OK":
    print ":: Opened mailbox, %s messages." % num_mails[0]

response, mails = connection.fetch('1:3', '(UID BODY[HEADER] BODY[TEXT])')
if response == "OK":
    print ":: Got messages."
    for rawMail in mails:
        mail = Mail(rawMail)
    
connection.logout()
