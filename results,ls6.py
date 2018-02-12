Python 3.6.3 (default, Oct  3 2017, 21:45:48) 
[GCC 7.2.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 
=============== RESTART: /home/cs2017a213/sahana/email,ls6.py ===============
Traceback (most recent call last):
  File "/home/cs2017a213/sahana/email,ls6.py", line 12, in <module>
    s.login("sender_email_id", "sender_email_id_password")
  File "/usr/lib/python3.6/smtplib.py", line 730, in login
    raise last_exception
  File "/usr/lib/python3.6/smtplib.py", line 721, in login
    initial_response_ok=initial_response_ok)
  File "/usr/lib/python3.6/smtplib.py", line 642, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials d74sm1222960pfb.54 - gsmtp')
>>> 
