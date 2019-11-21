import requests
from bs4 import BeautifulSoup
 
URL = "https://www.amazon.com/Razer-Blade-15-Smallest-i7-8750H/dp/B07D37VBVD/ref=sr_1_18?crid=1W4ID4KWM5AMP&keywords=razer+laptop&qid=1574347330&s=electronics&sprefix=razor%2Celectronics%2C813&sr=1-18"

headers = {"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

page = requests.get(URL, headers=headers)

