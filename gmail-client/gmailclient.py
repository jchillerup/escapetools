# encoding=utf8
''' Handle connecting, authentication and communication with gmail

    (c) 2013 escapetools crew

    All functions return True on success, False otherwise.

    Server data is read from self.response, as well as error messages.

'''

from imapclient import IMAPClient


def connectedAndAuthenticated(fn):
    ''' Decorator
    Ensure we are actually connected to the server before doing anything
    '''

    def wrapper(this, *args, **kwargs):
        this.response = None

        if this.connection and this.loggedIn:
            return fn(this, *args, **kwargs)
        else:
            # Should raise an error
            return 'Not authenticated'

    return wrapper


class GmailClient:
    ''' This is our gmail object

    Pass in username and password on init.
    Then call login to connect to server and authenticate.
    '''

    def __init__(self, username, password):
        self.imap_host = "imap.gmail.com"
        self.imap_port = 993
        self.imap_use_ssl = True
        self.imap_use_uid = True

        self.username = username
        self.password = password

        self.connection = None
        self.response = None

        self.loggedIn = False

    def login(self):
        ''' Log in
        No arguments

        Returns True on succesful log in
        Server response can be read from self.response
        '''

        try:
            self.connection = IMAPClient(
                self.imap_host,
                port=self.imap_port,
                ssl=self.imap_use_ssl,
                use_uid=self.imap_use_uid
            )
        except Exception as e:
            self.response = "Unable to connect to server: {0}".format(
                e.message
            )
            return False
        else:
            try:
                self.response = self.connection.login(
                    self.username,
                    self.password
                )
            except Exception as e:
                self.response = e.message
                return False
            else:
                self.loggedIn = True
                return True

    @connectedAndAuthenticated
    def logout(self):
        ''' Log out
            No arguments

            Returns True on succesful log out
            Server response can be read from self.response
        '''

        try:
            self.response = self.connection.logout()
        except Exception as e:
            self.response = e.message
            return False
        else:
            self.loggedIn = False
            return True

    @connectedAndAuthenticated
    def get_folders(self):
        ''' Return a list of folders

        '''

        try:
            self.response = self.connection.list_folders()
        except Exception as e:
            self.response = e.message
            return False
        else:
            return True

    @connectedAndAuthenticated
    def select_folder(self, folder):
        ''' Select a folder
        '''

        try:
            self.response = self.connection.select_folder(folder)
        except Exception as e:
            self.response = e.message
            return False
        else:
            return True

    @connectedAndAuthenticated
    def peek(self, messages):
        ''' Return from and subject for messages
            from folder currently selected by select_folder

        '''

        peekstr = 'BODY.PEEK[HEADER.FIELDS (FROM SUBJECT)]'
        dictstr = 'BODY[HEADER.FIELDS (FROM SUBJECT)]'

        returnlist = {}

        try:
            if self.fetch(messages, data=[peekstr, 'RFC822.SIZE', 'FLAGS']):
                for m_id in self.response:
                    returnlist[m_id] = {}
                    returnlist[m_id]['flags'] = self.response[m_id]['FLAGS']
                    returnlist[m_id][
                        'subjectfrom'] = self.response[m_id][dictstr]

            self.response = returnlist

        except Exception as e:
            self.response = e.message
            return False
        else:
            return True

    @connectedAndAuthenticated
    def fetch(self, messages, data=['RFC822', 'FLAGS'], modifiers=None):
        ''' Fetch one or more mails according to messages dict, ie. [1, 55, 32]

        '''

        try:
            self.response = self.connection.fetch(messages, data, modifiers)
        except Exception as e:
            self.response = e.message
            return False
        else:
            return True
