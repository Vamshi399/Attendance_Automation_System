import os,sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime

def mailsend(toaddr,msgbody):

    fromadrs="aasbychargers@gmail.com"
    password = "team2chargers"
    msg = MIMEMultipart()
    msg['From'] = fromadrs
    msg['To'] = toaddr
    msg['Subject'] = f"Absent Attendance Data {datetime.today().strftime('%Y-%m-%d')}"
    body = msgbody
    html = """
    <html>
      <head></head>
      <body>
        <h2>
        Please find the below list of students absent for today : {day}
        </h2>
        <p>
        {body1}
        </p>
      </body>
    </html>
    """.format(body1=body,day=datetime.today().strftime('%Y-%m-%d'))
    html1 = """
        <html>
          <head></head>
          <body>
            <h2>
            No Student is absent for today
            </h2>
          </body>
        </html>
        """
    if body=='':
        #body='No Students are absent for today'
        msg.attach(MIMEText(html1, 'html'))
    else:
        msg.attach(MIMEText(html,'html'))
        #msg.attach(MIMEText(body, 'plain'))
    #msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo
    server.starttls()
    server.login(fromadrs, password)
    text = msg.as_string()
    server.sendmail(fromadrs, toaddr, text)
    server.quit()
    print("sent email")


#str="<html><table><tr><td>hi</td></tr></table></html>"
str="<html><h1>Please find the below list of student absent for today</h1></html>"
