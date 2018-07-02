import requests, datetime, base64
from requests.auth import HTTPBasicAuth

url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest" #C2B URL

def access_token():
    consumer_key = "dCAjsR40OL23JkI6IIZTwaDIWzZh8Q7g"  #This must be unique
    consumer_secret = "SGoKEryVJZvMYNO6"  # this one too
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials" #AUTH URL
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    data = r.json()
    access_token = "Bearer" + ' ' + data['access_token']

    return access_token


def password_key(business_short_code, passkey, timestamp):
    data = business_short_code + passkey + timestamp
    encoded = base64.b64encode(data.encode())
    password = encoded.decode('utf-8')

    return  password


def payload():
    timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
    passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
    business_short_code = "174379"

    data = {
            "BusinessShortCode": business_short_code,
            "Password": password_key(business_short_code, passkey, timestamp),
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

    return data

def hearders():
    headers = {
        "Authorization": access_token(),
        "Content-Type": "application/json"
    }

    return headers

def payload_send(link):
    request = requests.post(link, json=payload(), headers=hearders())

    print (request.json())


payload_send(url)
