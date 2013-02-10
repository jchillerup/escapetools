class Mail:
    """A data container for the GMail fetcher"""

    uid = None
    headers = None
    body = None
    attachments = []
    unread = None
    
    def __init__(self, rawMail):
        pass
