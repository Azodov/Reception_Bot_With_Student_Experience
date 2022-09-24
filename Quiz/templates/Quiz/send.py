
import smtplib, ssl
## email.mime subclasses
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
### Add new subclass for adding attachments
from email.mime.application import MIMEApplication
## The pandas library is only for generating the current date, which is not necessary for sending emails
import pandas as pd

# Define the HTML document
# Add an image element
##############################################################
html = '''
    <html>
        <body>
            <h1>Daily S&P 500 prices report</h1>
            <p>Hello, welcome to your report!</p>
            <img src='cid:myimageid' width="700">
        </body>
    </html>
    '''
##############################################################

# Define a function to attach files as MIMEApplication to the email
    ## Add another input extra_headers default to None
##############################################################

##############################################################    

# Set up the email addresses and password. Please replace below with your email address and password
email_from = "bekhruz.rich@outlook.com"
password = '258182126rich'
email_to = 'bekhruz.rich@gmail.com'

# Generate today's date to be included in the email Subject
date_str = pd.Timestamp.today().strftime('%Y-%m-%d')

# Create a MIMEMultipart class, and set up the From, To, Subject fields
email_message = MIMEMultipart()
email_message['From'] = email_from
email_message['To'] = email_to
email_message['Subject'] = f'Report email - {date_str}'

# Attach the html doc defined earlier, as a MIMEText html content type to the MIME message
email_message.attach(MIMEText(html, "html"))

# Attach more (documents)
  ## Apply function with extra_header on chart.png. This will render chart.png in the html content
##############################################################


# Convert it as a string
email_string = email_message.as_string()

# Connect to the Gmail SMTP server and Send Email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.outlook.com", 465, context=context) as server:
    server.login(email_from, password)
    server.sendmail(email_from, email_to, email_string) 