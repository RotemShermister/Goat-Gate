import smtplib
import credentials #contains passwords and emails (not to be uploaded to git)


# global variables
email = credentials.sender
reciever_email = credentials.receiver
server = smtplib.SMTP("smtp.gmail.com",587) 

# start ttls and login
def initialize():
    server.starttls()
    server.login(email, credentials.password)


# send an email for when the gate is opened
def send_open():

    subject = "GOAT GATE"
    message = "WHO LET THE GOATS OUT?! \n\nFiona & Marceline are out on the loose. \n\nIf it is you, great! If not, GO GET THEM!!!" 

    text = "Subject:"+ subject +"\n\n" + message 

    server.sendmail(email, reciever_email, text)

    print("Email has been sent to " + reciever_email)


# main : (delete when integrated with switch)
initialize()
send_open()