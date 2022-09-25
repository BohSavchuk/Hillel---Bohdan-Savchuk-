from typing import Any
import requests
import pprint
import validators
import smtplib
import datetime
import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
#import validate_email from validate_email
from functools import lru_cache

SMTP_SERVER = 'smtp.ukr.net'
PASSWORD_API = 'EdJHkfTfN2uFmAeZ'
USER_ = 'hillelbohdan@ukr.net'
password_for_email = 'bohdan007'


URL_EMAILS = 'https://script.google.com/macros/s/AKfycby3Fp-J3N0OM5UZhg9SHgIusHBMC2kWVXSOVsP26smPTaYS_4IiOT7sVx7ZWyC3XsVW7g/exec'
URL_WEATHER = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=47503e85fabbabc93cff28c52398ae97&units=metric'


message = 'Ola,amigo {}!Please see information about weather on {}, in {}.Temperature: {}, {} {}, humidiy:{}, pressure{}'


weather_icons = {
      '01d': '\U0001F305',
      '01n': '\U0001F311',
      '02d': '\U00002601',
      '02n': '\U00002601',
      '03n': '\U00002601',
      '03d': '\U00002601',
      '04d': '\U0001F325',
      '04n': '\U0001F325',
      '09d': '\U00002614',
      '09n': '\U00002614',
      '50d': '\U0001F32B',
      '13d': '\U000026C4',
}





def get_data (func):
        """
        The function will receive data from url
          Args:
              url: str

          Returns: dict
          """
        def wrapper (url):
                response = requests.get(url)
                data = response.json()
                func(data['data'])
        return wrapper



def emails_validator (func):
        """
        This function validate emails
        Args(function):

        Returns: emails_list

        """
        def wrapper(emails_list):
                valid_emails = []
                for mails in emails_list:
                    if validators.email(mails['e_mail']):
                        valid_emails.append(mails)
                func(valid_emails)
        return wrapper


@lru_cache(maxsize=10)
@get_data
@emails_validator
def mail_sender(recipient):
    """
    sending e-mail with a receipt
    """
    now = datetime.datetime.now().date()
    for value in recipient:
        city = URL_WEATHER.format(value['city'])
        response = requests.get(city)
        data = response.json()
        datetime.datetime.now()
        if data['weather'][0]['icon'] in weather_icons:
            email_to_client = message.format(value['name'], now, value['city'], data['main']['feels_like'], data['weather'][0]['main'], weather_icons[data['weather'][0]['icon']], data['main']['humidity'], data['main']['pressure'])

    server = SMTP_SERVER
    PASSWORD = PASSWORD_API
    USER = USER_

    recipient = [value['e_mail']]
    sender = USER
    subject = 'Bohdan Savchuk Weather'
    text = email_to_client

    # for sending a file-----------------
  #  filepath = "mail66.py"

   # from os.path import exists
    #file_exists = exists(filepath)
    #if not file_exists:
     #   print('file unavailable')
      #  return False
    #basename = os.path.basename(filepath)
    #filesize = os.path.getsize(filepath)
    # ------------------------------------

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = 'Python script <' + sender + '>'
    msg['To'] = ', '.join(recipient)
    msg['Reply-To'] = sender
    msg['Return-Path'] = sender
    msg['X-Mailer'] = 'decorator'

    part_text = MIMEText(text, 'plain')

    # for sending a file----------------------------------------------------------------------
 #   part_file = MIMEBase('application', 'octet-stream; name="{}"'.format(basename))
  #  part_file.set_payload(open(filepath, "rb").read())
   # part_file.add_header('Content-Description', basename)
   # part_file.add_header('Content-Disposition', 'attachment; filename="{}"; size={}'.format(basename, filesize))
   # encoders.encode_base64(part_file)
   # msg.attach(part_file)
    # ----------------------------------------------------------------------------------------

    msg.attach(part_text)

    mail = smtplib.SMTP_SSL(server)
    mail.login(USER, PASSWORD)
    mail.sendmail(sender, recipient, msg.as_string())
    mail.quit()
    return True

#mail_sender(('test_hillel_api_mailing@ukr.net', 'w.i.k.mailua@gmail.com'), 'kldsgvjdf')



mail_sender(URL_EMAILS)

