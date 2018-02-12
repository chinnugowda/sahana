# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib
 
# creates SMTP session
server = smtplib.SMTP('smtp.gmail.com', 587)
 
# start TLS for security
server.starttls()
 
# Authentication
server.login("sahana.17cs@cmr.edu.in", "...")
 
# message to be sent
message = "hi hello"
 
# sending the mail
server.sendmail("sahana.17cs@cmr.edu.in", "sahanagowda257@gmail.com", message)
 
# terminating the session
server.quit()
