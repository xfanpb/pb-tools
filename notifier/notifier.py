import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

username = "sample gmail account"
password = "applicationpassword"
mail_from = "same email"
mail_to = "target"
mail_subject = "Test Subject"
mail_body = "This is a test message"

mimemsg = MIMEMultipart()
mimemsg['From']=mail_from
mimemsg['To']=mail_to
mimemsg['Subject']=mail_subject
mimemsg.attach(MIMEText(mail_body, 'plain'))
connection = smtplib.SMTP(host='smtp.gmail.com', port=587)
connection.starttls()
connection.login(username,password)
connection.send_message(mimemsg)
connection.quit()