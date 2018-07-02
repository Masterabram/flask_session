import requests
import datetime
import base64
from requests.auth import HTTPBasicAuth

#GENERATING THE ACCESS TOKEN
consumer_key = "dCAjsR40OL23JkI6IIZTwaDIWzZh8Q7g"  #This must be unique
consumer_secret = "SGoKEryVJZvMYNO6"  # this one too

api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials" #AUTH URL

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

data = r.json()
access_token = "Bearer" + ' ' + data['access_token']

#GETTING THE PASSWORD
timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
business_short_code = "174379"
data = business_short_code + passkey + timestamp
encoded = base64.b64encode(data.encode())
password = encoded.decode('utf-8')


# BODY OR PAYLOAD
payload = {
  "BusinessShortCode": business_short_code,
  "Password": password,
  "Timestamp": timestamp,
  "TransactionType": "CustomerPayBillOnline",
  "Amount": 10,
  "PartyA": 254790463533,
  "PartyB": business_short_code,
  "PhoneNumber": 254790463533,
  "CallBackURL": "http://mpesa-requestbin.herokuapp.com/15kzjtu1",
  "AccountReference": "test",
  "TransactionDesc": "test"
}

#POPULAING THE HTTP HEADER
headers = {
    "Authorization": access_token,
    "Content-Type": "application/json"
    }

url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest" #C2B URL

response = requests.post(url, json=payload, headers=headers)

print (response.text)

