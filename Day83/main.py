import smtplib

# https://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python
fromaddr = 'christianwebdeveloper57@gmail.com'
toaddrs = 'billhall105@yahoo.com'
msg = "\r\n".join([
      "From: christianwebdeveloper57@gmail.com",
    "To: billhall105@gmail.com",
    "Subject: This is a test message",
    "",
    "Is this working?"
    ])

username = 'christianwebdeveloper57@gmail.com'
password = '5nH1O%Cj4nA1%h'
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username, password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
