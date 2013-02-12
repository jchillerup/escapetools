from getpass import getpass
from gmailclient import GmailClient as Gmail

print("#####################")
print("#                   #")
print("# Gmail IMAP client #")
print("#                   #")
print("#####################")
print("")
print("")

user = raw_input('User     : ')
password = getpass('Password : ')

# Create gmail object
g = Gmail(user, password)

print("Connecting ...")
# Connect and login
if not g.login():
    print("Error logging in - exiting")

else:
    print("Logged in")
    print("")

    print("Folders : ")

    if g.get_folders() :
        for folder in g.response:
            # Display folder name
            print folder[2]

        print("")

        inspect = raw_input("Show messages in folder : ")

        if g.select_folder(inspect):
            msg_count = g.response['EXISTS']
            msg_range = range(1, int(msg_count)+1)

            print("")
            if g.peek(msg_range):
                for msg_n in g.response:
                    # Print subject and from
                    print g.response[msg_n]
