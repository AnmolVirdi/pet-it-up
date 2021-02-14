import smtplib 
import config_mail as config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send(reciver,message):
    sender = config.MAIL_USERNAME
    password = config.MAIL_PASSWORD

    msg = MIMEMultipart()

    msg['From'] = sender
    msg['To'] = reciver
    msg['Subject'] = 'Petitup | Confirmation Link'
    body = message
    msg.attach(MIMEText(body,'plain'))
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    
    # start TLS for security 
    s.starttls() 
    
    # Authentication 
    s.login(sender, password) 
    
    # message to be sent 
    text = msg.as_string()
    
    # sending the mail 
    s.sendmail(sender,reciver, text) 
    
    # terminating the session 
    s.quit() 
    return