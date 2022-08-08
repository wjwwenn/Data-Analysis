import email
import imaplib # imap pop

username = 'wjingwen96@gmail.com'
password = '' # app password

mail = imaplib.IMAP4_SSL("imap.gmail.com")
# https://www.google.com/settings/security/lesssecureapps
mail.login(username, password)
mail.select("inbox") 
mail.create("Item") # create new folder
mail.list() # list folders

result, data = mail.uid('search', None, "ALL")
inbox_item_list = data[0].split()
most_recent = inbox_item_list[-1]
oldest = inbox_item_list[0]

# ---------- Fetching oldest email
result2, email_data = mail.uid('fetch', oldest, '(RFC822)')
raw_email = email_data[0][1].decode("utf-8")
email_message = email.message_from_string(raw_email)
# dir(email_message)

email_message['To']
email_message['From']
email_message['Subject']