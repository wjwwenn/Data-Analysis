import smtplib

host = "smtp.gmail.com"
port = 587
username = "wjingwen96@gmail.com"
password = "zumlxfuvbmkhztod"
from_email = username
to_list = ["wjingwen96@gmail.com"]

email_conn = smtplib.SMTP(host, port)
email_conn.ehlo() # to check if it is connected
email_conn.starttls() # ready to start
email_conn.login(username, password) # login with 16-digit app password as original acc has 2 FA
email_conn.sendmail(from_email, to_list, "hello there, this is a message")
email_conn.quit()

from smtplib import SMTP
ABC = SMTP(host, port)
ABC.ehlo()
ABC.starttls()
ABC.login(username, password)
ABC.sendmail(from_email, to_list, "hello, this is a message")
ABC.quit()

from smtplib import SMTP, SMTPAuthenticationError, SMTPException
pass_wrong = SMTP(host, port)
pass_wrong.ehlo()
pass_wrong.starttls()
try:
    pass_wrong.login(username, password)
    pass_wrong.sendmail(from_email, to_list, "hello, this is a message")
except:
    print("an error occurred")    

pass_wrong.quit()