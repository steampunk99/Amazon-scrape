import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.com/Razer-Blade-15-Smallest-i7-8750H/dp/B07D37VBVD/ref=sr_1_18?crid=1W4ID4KWM5AMP&keywords=razer+laptop&qid=1574347330&s=electronics&sprefix=razor%2Celectronics%2C813&sr=1-18"

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    price = soup.find(id="priceblock_ourprice").get_text()

    converted_price = float(price[0:5])

    if(converted_price <= 1000):
        send_mail()

    print(title.strip())
    print(converted_price)


def send_mail():
    # the number is gmail's connection number#
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()  # Is an extended simple mail transfer protocal sent by an email server to identify itself when connecting to another server
    server.starttls()  # This is to encrpyt our connection
    server.ehlo()

    # PS-The password was generated using google app passwords and only works once on my mac only
    server.login('luk23bonnie8@gmail.com', 'aaunvgbtxyblhnby')
    subject = "Yo, the price of the pc fell"
    body = "Check the amazon link--> https://www.amazon.com/Razer-Blade-15-Smallest-i7-8750H/dp/B07D37VBVD/ref=sr_1_18?crid=1W4ID4KWM5AMP&keywords=razer+laptop&qid=1574347330&s=electronics&sprefix=razor%2Celectronics%2C813&sr=1-18 "

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'luk23bonnie8@gmail.com',  # from
        'luk23bonnie8@gmail.com',  # recipient
         msg
    )
