import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
import configparser

config = configparser.RawConfigParser()
config.read('mail.properties')
host_address = config.get('EmailSection','host.address')
port_number = config.get('EmailSection','port.number')
username = config.get('EmailSection','email.username')
password = config.get('EmailSection','email.password')

email = EmailMessage()
email['from'] = 'Tester'
email['to'] = '<to email address>'
email['subject'] = 'testing email !'

html_content = Template(Path('email_content.html').read_text())
email.set_content(html_content.substitute({'name':'Tin Tin'}), 'html')

#need to turn on https://myaccount.google.com/lesssecureapps
with smtplib.SMTP(host=host_address, port=port_number) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(username, password)
    smtp.send_message(email)
    print("email has been sent out successfully!")