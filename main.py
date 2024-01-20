import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.com/CyberpowerPC-Xtreme-i7-12700F-GeForce-GXiVR8040A12/dp/B09TCKBJC3/ref=sr_1_4?keywords=gaming%2Bcomputer&qid=1676978861&sr=8-4&th=1'
HEADER = {
    'Accept-Language': 'en-US,en;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}
EMAIL_SUBJECT = 'Gaming PC'
# FINDING THE PRICE OF A PRODUCT ON AMAZON
web_page = requests.get(url=URL, headers=HEADER).text

soup = BeautifulSoup(web_page, 'html.parser')

price = float(soup.find(class_='a-price-whole').get_text().replace(',', ''))
print(price)
print(type(price))


# SENDING AN EMAIL IF THE PRICE OF THAT PRODUCT IS WHAT WE'RE WILLING TO PAY
if price < 2000:
    my_email = 'email@gmail.com'
    my_password = 'password'

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs='email@yahoo.com', msg=f'Subject:{EMAIL_SUBJECT}\n\nGreat news! Your {EMAIL_SUBJECT} is at an affordable price, get it now! \n{URL}')







