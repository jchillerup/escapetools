#!/usr/bin/python

''' This test file is specific to a test account we have made on the gmail email system
    You can test it yourself by creating a label called "X A" (without the quotes that is)
    and running this script - spoiler : it breaks - but why?
'''

import sys
import imaplib as imap
import getpass
import re
from mail_class import Mail

connection = imap.IMAP4_SSL("imap.gmail.com", 993)

print(":: Logging into GMail")

connection.login(input("Username: ") if sys.version_info[0] >= 3 else raw_input("Username: "), getpass.getpass())

print(":: Logged in, enumerating mailboxes")

response, mailboxes = connection.list()

if response == "OK":
    for mailbox in mailboxes:
        print (" - {0}".format(mailbox.decode("utf-8")))
else:
    sys.stderr.write("Failed to enumerate mailboxes, exiting.\n")
    sys.exit(1)


print "-------------------------"
response, num_mails = connection.select("X A", True)
print('When trying to connect directly to "X A" : %s' % (response,))

print "-------------------------"

for mailbox in mailboxes:
    print("Mailbox : %s" % (mailbox,))
    m = re.match("\((.*?)\)\s{1,}\"(.*?)\"\s\"(.*?)\"$", mailbox.decode("utf-8"))
    tags, path, mailboxname = (m.group(1).lstrip("\\").split(" \\"), m.group(2), m.group(3))
    print("Mailbox name : %s" % (mailboxname,))

    if "HasChildren" in tags: #These fail to open
        continue

    print("")
    print('Is it the "X A" mailbox : %s' % (mailboxname == 'X A'))
    response, num_mails = connection.select(mailboxname, True)
    print('Server response : %s' % (response, ))

connection.logout()
