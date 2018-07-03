# MPESA DOCUMENTATION
In this project I was doing a simple project on MPESA API using the LIPA NA MPESA express API. The express API, just enables one to finetune its code such that when it runs, the user/client just sees a pop up asking him to input the password. 

----

## Running the application
  
  * clone the repo
  * Run the MPESAV3.py file

----

A normal and usual MPESA API will have three main parts,
  * The Authentication. 
  * Headers. 
  * Body/Payload.
 
---

## Authetication

When you create an app in [Safaricom developer](developer.safaricom.co.ke) under the app dashboard, the app will be assigned a <b>consumer key</b> and <b>consumer secret</b>.
To authorize your API call to the OAuth API, you will need a Basic Auth over HTTPS authorization token. username = `consumer key` and password = `consumer secret`

```
def access_token():
    consumer_key = " " 
    consumer_secret = " " 
    
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    data = r.json()
    
    access_token = "Bearer" + ' ' + data['access_token']

    return access_token 
    
  ```
When the the request is made, the response is a text usually forrmated as a json. To convert this to json, you have to use the  `.json()` fuction.  

Request

  `r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))` 

Response

```
{
    "access_token": "5G2MZGkAqIuklAsRdKAT15yad2n2",
    "expires_in": "3599"
}
```

However, the only important thing we need is the `access_token` object.

`access_token = "Bearer" + ' ' + data['access_token']`

---

## Headers

The HTTP headers needed by the API is one that contains the `Authorization` and `Content-type`
```
headers = {
        "Authorization": "Bearer" % Access token,
        "Content-Type": "application/json"
    }
```
The acccess token in this case was returned from the `access_token()` function we previously had.

---

## Body
This is how a sample payload looks like and most of this documentation and illustrations can be found [here](https://developer.safaricom.co.ke/lipa-na-m-pesa-online/apis/post/stkpush/v1/processrequest) .
```
{
      "BusinessShortCode": "",
      "Password": "",
      "Timestamp": "",
      "TransactionType": "CustomerPayBillOnline",
      "Amount": "",
      "PartyA": "",
      "PartyB": "",
      "PhoneNumber": "",
      "CallBackURL": "",
      "AccountReference": "",
      "TransactionDesc": ""
  }
```

Let's take a dive into each object above:
* `BusinessShortCode` gotten from the test credentials and refers to the `The organization shortcode used to receive the transaction`
* `Password` this is probably the most complex. its is gotten by `base64() Encoding` then concatenated `BusinessShortCode` + `Passkey` (gotten from the test credentials) and `timestamp` (14 characters current timestamp in this format `YYYYMMDDHHiiss`)

```
def password_key(business_short_code, passkey, timestamp):
    data = business_short_code + passkey + timestamp
    encoded = base64.b64encode(data.encode())
    password = encoded.decode('utf-8')

    return  password
```
The fuction above takes in the `business_short_code, passkey & timestamp` and returns out the hashed <b>base64 encoded password</b>

  * `CallBackURL` is a HTTP listening server Url where all MPESA [response codes are sent](https://developer.safaricom.co.ke/docs#m-pesa-result-and-response-codes). In my case I used [http://mpesa-requestbin.herokuapp.com](http://mpesa-requestbin.herokuapp.com) to generate a callback url.

The rest of the objects in the payload can be found and defined within the documentation and as a result here is a sample payload fuction I had.

```
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
```

---

To send all the requests and listen fot the response, I use the the following function
```
def payload_send(link):
    request = requests.post(link, json=payload(), headers=hearders())

    print (request.json())
```
where the `link` refers to the URL of the transaction endpoint route. 

Thank you and Have a blast.
+254790463533
