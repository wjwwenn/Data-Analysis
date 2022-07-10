from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

host = "smtp.gmail.com"
port = 587
username = "wjingwen96@gmail.com"
password = "" # use gmail 16 digit app password
from_email = username
to_email = username
# to_list = ["wjingwen96@gmail.com"]

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Sample email"
msg['From'] = from_email
msg['To'] = to_email

# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
html = """\
<html>
    <head></head>
    <body>
        <p>Hey!<br>
        Testing the email <b>message</b>, made by <a href='http://joincfe.com'>Team CFE</a>,
        </p>
    </body>
</html>
    """

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)

# Send the message via local SMTP server.
#s = smtplib.SMTP('smtp.gmail.com.')
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(username, password)

# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
smtpserver.sendmail(from_email, to_email, msg.as_string())
smtpserver.quit()
