#!/usr/bin/python2

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

for mailbox in mailboxes:
    m = re.match("\((.*?)\)\s{1,}\"(.*?)\"\s\"(.*?)\"$", mailbox.decode("utf-8"))
    tags, path, mailbox = (m.group(1).lstrip("\\").split(" \\"), m.group(2), m.group(3))
    if "HasChildren" in tags: #These fail to open
        continue

    response, num_mails = connection.select(mailbox, True)
    if response == "OK":
        print(":: Opened {0}, {1} messages.".format(mailbox, num_mails[0].decode("utf-8")))

        response, mails = connection.fetch('1:3', '(UID BODY[HEADER] BODY[TEXT])')
        if response == "OK":
            for rawMail in mails:
                mail = Mail(rawMail)

connection.logout()
