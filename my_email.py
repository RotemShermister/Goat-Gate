import smtplib
import credentials  # contains passwords and emails (not to be uploaded to git)
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# global variables
email = credentials.sender
reciever_email = credentials.receiver
server = smtplib.SMTP("smtp.gmail.com", 587)


# start ttls and login
def initialize():
    server.starttls()
    server.login(email, credentials.password)


# send an email for when the gate is opened
def send_open():
    subject = "GOAT GATE"

    # Short HTML with inline image reference (I had to google this)
    # https://stackoverflow.com/questions/920910/sending-multipart-html-emails-which-contain-embedded-images
    html = """
    <p>WHO LET THE GOATS OUT?!</p>
    <p>Fiona & Marceline are out on the loose.</p>
    <p>If it is you, great! If not, <strong>GO GET THEM!!!</strong></p>
    <img src="cid:goatimage">
    """

    # Create the multipart message
    msg = MIMEMultipart('related')
    msg['Subject'] = subject
    msg['From'] = email
    msg['To'] = reciever_email

    # Add HTML part
    msg.attach(MIMEText(html, 'html'))

    # Attach image with Content-ID for inline display
    with open("pic.jpg", 'rb') as img_file:
        img = MIMEImage(img_file.read())
        img.add_header('Content-ID', '<goatimage>')  # matches the cid:goatimage in HTML
        msg.attach(img)

    # Send the email
    server.sendmail(email, reciever_email, msg.as_string())
    print("Email with inline image has been sent to " + reciever_email)


# main : (delete when integrated with switch)
#initialize()
#send_open()
