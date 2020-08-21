from imapclient import IMAPClient
mail = IMAPClient('imap.gmail.com', ssl=True, port=993)
mail.login("example@gmail.com", "password")
totalMail = mail.select_folder('Inbox')
#Shows how many messages are there - both read and unread
print('You have total %d messages in your folder' % totalMail[b'EXISTS'])
delMsg = mail.search(('UNSEEN'))
mail.delete_messages(delMsg)
#Shows number of unread messages that have been deleted now
print('%d unread messages in your folder have been deleted' % len(delMsg))
mail.logout()

#source => https://www.linkedin.com/pulse/deleting-unread-emails-from-gmail-once-python-moumita-das/?articleId=6602551122534207488
